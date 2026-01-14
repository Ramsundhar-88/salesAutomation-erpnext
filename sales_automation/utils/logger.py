import frappe


def log(title:str, message:str):
    """
    central place for logging.
    In production, You can upgrade  this to a usea custom Doctype logger."""
    frappe.log_error(message=message, title=title)
