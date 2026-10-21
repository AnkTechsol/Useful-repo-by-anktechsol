#!/usr/bin/env python3
"""Offline GSTIN / PAN format checks and GST split calculator. Standard library only.

Usage:
  python3 gst_check.py gstin 27AAPFU0939F1ZV
  python3 gst_check.py pan AAPFU0939F
  python3 gst_check.py split --taxable 10000 --rate 18 --seller-state 27 --place-of-supply 29

These checks only test format and checksum. They do NOT confirm the number is
registered or active. Verify status on the official GST portal.
"""
import argparse
import json
import re
import sys

CHARSET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
GSTIN_RE = re.compile(r"^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][1-9A-Z]Z[0-9A-Z]$")
PAN_RE = re.compile(r"^[A-Z]{5}[0-9]{4}[A-Z]$")
PAN_TYPES = {
    "P": "Individual", "C": "Company", "H": "HUF", "F": "Firm/LLP",
    "A": "Association of Persons", "T": "Trust", "B": "Body of Individuals",
    "L": "Local Authority", "J": "Artificial Juridical Person", "G": "Government",
}


def gstin_checksum(first14: str) -> str:
    total = 0
    for i, ch in enumerate(first14):
        product = CHARSET.index(ch) * (1 if i % 2 == 0 else 2)
        total += product // 36 + product % 36
    return CHARSET[(36 - total % 36) % 36]


def check_gstin(value: str) -> dict:
    v = value.strip().upper()
    out = {"input": v, "valid_format": False, "valid_checksum": False, "notes": []}
    if not GSTIN_RE.match(v):
        out["notes"].append("Does not match the 15-character GSTIN pattern.")
        return out
    out["valid_format"] = True
    out["state_code"] = v[:2]
    out["embedded_pan"] = v[2:12]
    out["entity_number"] = v[12]
    expected = gstin_checksum(v[:14])
    out["valid_checksum"] = expected == v[14]
    if not out["valid_checksum"]:
        out["notes"].append(f"Checksum mismatch: expected last character {expected}.")
    pan = check_pan(v[2:12])
    if not pan["valid_format"]:
        out["notes"].append("Embedded PAN has an invalid format.")
    else:
        out["pan_holder_type"] = pan["holder_type"]
    out["notes"].append("Format and checksum only. Confirm registration status on the GST portal.")
    return out


def check_pan(value: str) -> dict:
    v = value.strip().upper()
    ok = bool(PAN_RE.match(v))
    return {
        "input": v,
        "valid_format": ok,
        "holder_type": PAN_TYPES.get(v[3], "Unknown") if ok else None,
        "notes": ["Format only. This does not verify the PAN with the tax department."],
    }


def split_gst(taxable: float, rate: float, seller_state: str, place_of_supply: str) -> dict:
    tax = round(taxable * rate / 100, 2)
    if seller_state == place_of_supply:
        half = round(tax / 2, 2)
        return {"type": "intra-state", "cgst": half, "sgst": round(tax - half, 2),
                "igst": 0.0, "total_tax": tax, "invoice_total": round(taxable + tax, 2)}
    return {"type": "inter-state", "cgst": 0.0, "sgst": 0.0, "igst": tax,
            "total_tax": tax, "invoice_total": round(taxable + tax, 2)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("gstin"); g.add_argument("value")
    p = sub.add_parser("pan"); p.add_argument("value")
    s = sub.add_parser("split")
    s.add_argument("--taxable", type=float, required=True)
    s.add_argument("--rate", type=float, required=True)
    s.add_argument("--seller-state", required=True, help="2-digit GST state code of the supplier")
    s.add_argument("--place-of-supply", required=True, help="2-digit state code of place of supply")
    a = ap.parse_args()
    if a.cmd == "gstin":
        res = check_gstin(a.value)
    elif a.cmd == "pan":
        res = check_pan(a.value)
    else:
        res = split_gst(a.taxable, a.rate, a.seller_state, a.place_of_supply)
    print(json.dumps(res, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
