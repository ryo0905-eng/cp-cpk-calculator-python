from __future__ import annotations

from flask import Response, render_template, request, send_file, url_for

from content.pages import CONTENT_PAGES, get_page_faqs, get_related_pages
from data.sample_catalog import SAMPLE_OPTIONS, build_sample_file
from services.calculator import (
    CALCULATOR_PAGE,
    build_initial_calculator_state,
    get_form_state,
    run_calculation,
)
from services.doe import DOE_PAGE, build_doe_plan, build_initial_doe_state, get_doe_form_state

GUIDE_PRIORITY_ORDER = [
    "cp-vs-cpk",
    "what-is-a-good-cpk-value",
    "how-to-calculate-cp-cpk",
    "what-is-cpk",
    "what-is-cp",
    "cp-formula",
    "what-is-pp-ppk",
    "pp-vs-ppk",
]


def build_base_context(**kwargs) -> dict:
    base_url = request.url_root.rstrip("/")
    return {
        "base_url": base_url,
        "canonical_url": f"{base_url}{request.path}",
        "sample_options": SAMPLE_OPTIONS,
        **kwargs,
    }


def register_routes(app) -> None:
    @app.route("/", endpoint="index")
    def index():
        return render_template(
            "home.html",
            **build_base_context(
                page_title="Manufacturing & Statistics Tools | Free Cp/Cpk and DoE Tools",
                meta_description="Free manufacturing and statistics tools for practical engineering work. Use the Cp/Cpk calculator and DoE planner to evaluate capability and plan experiments.",
            ),
        )

    @app.route("/cp-cpk-calculator", methods=["GET", "POST"], endpoint="cp_cpk_calculator")
    def cp_cpk_calculator():
        state = build_initial_calculator_state()

        if request.method == "POST":
            state["form"] = get_form_state(request.form)
            try:
                state.update(run_calculation(state["form"], request.files.get("uploaded_file")))
            except Exception as exc:
                state["error_message"] = str(exc)

        return render_template(
            "index.html",
            **build_base_context(
                page_title=CALCULATOR_PAGE["page_title"],
                meta_description=CALCULATOR_PAGE["meta_description"],
                **state,
            ),
        )

    @app.route("/guides", endpoint="guides")
    def guides():
        guide_pages = []

        for slug in GUIDE_PRIORITY_ORDER:
            page = CONTENT_PAGES.get(slug)
            if page is None:
                continue
            guide_pages.append(
                {
                    "slug": slug,
                    "title": page["title"],
                    "heading": page["heading"],
                    "description": page["description"],
                }
            )

        return render_template(
            "guides.html",
            **build_base_context(
                page_title="Process Capability Guides | Cp, Cpk, Pp, and Ppk Articles",
                meta_description="Browse practical guides about Cp, Cpk, Pp, Ppk, and process capability analysis, then jump into the tools when you are ready to use them.",
                guide_pages=guide_pages,
            ),
        )

    @app.route("/download/<sample_key>.csv", endpoint="download_sample")
    def download_sample(sample_key: str):
        sample_file = build_sample_file(sample_key)
        if sample_file is None:
            return Response("Not found", status=404)

        file_obj, filename = sample_file
        return send_file(
            file_obj,
            mimetype="text/csv",
            as_attachment=True,
            download_name=filename,
        )

    @app.route("/robots.txt", endpoint="robots")
    def robots():
        lines = [
            "User-agent: *",
            "Allow: /",
            f"Sitemap: {request.url_root.rstrip('/')}{url_for('sitemap')}",
        ]
        return Response("\n".join(lines), mimetype="text/plain")

    @app.route("/healthz", endpoint="healthz")
    def healthz():
        return Response("ok", mimetype="text/plain")

    @app.route("/sitemap.xml", endpoint="sitemap")
    def sitemap():
        pages = [{"loc": request.url_root.rstrip("/") + url_for("index"), "priority": "1.0"}]
        pages.append({"loc": request.url_root.rstrip("/") + url_for("cp_cpk_calculator"), "priority": "0.9"})
        pages.append({"loc": request.url_root.rstrip("/") + url_for("doe_planner"), "priority": "0.9"})
        pages.append({"loc": request.url_root.rstrip("/") + url_for("guides"), "priority": "0.8"})
        for slug in CONTENT_PAGES:
            pages.append(
                {
                    "loc": request.url_root.rstrip("/") + url_for("content_page", slug=slug),
                    "priority": "0.8",
                }
            )

        return render_template("sitemap.xml", pages=pages), 200, {"Content-Type": "application/xml"}

    @app.route("/doe-planner", methods=["GET", "POST"], endpoint="doe_planner")
    def doe_planner():
        state = build_initial_doe_state()

        if request.method == "POST":
            state["form"], state["factor_fields"] = get_doe_form_state(request.form)
            try:
                state.update(build_doe_plan(state["form"]))
            except Exception as exc:
                state["error_message"] = str(exc)

        return render_template(
            "doe_planner.html",
            **build_base_context(
                page_title=DOE_PAGE["page_title"],
                meta_description=DOE_PAGE["meta_description"],
                **state,
            ),
        )

    @app.route("/<slug>", endpoint="content_page")
    def content_page(slug: str):
        page = CONTENT_PAGES.get(slug)
        if page is None:
            return Response("Not found", status=404)

        return render_template(
            "content_page.html",
            **build_base_context(
                page_title=page["title"],
                meta_description=page["description"],
                page=page,
                page_slug=slug,
                related_pages=get_related_pages(slug),
                faqs=get_page_faqs(slug),
            ),
        )
