def after_insert(doc, method=None):
    # Auto-set source if missing
    if not doc.get("source"):
        doc.source = "Website"
        doc.save(ignore_permissions=True)
