
import re
from urllib.parse import urlparse


# Explanations for each warning sign
REASONS = {
    "Contains an @ symbol; inspect carefully.":
        "Text before @ can mislead someone about the actual destination.",

    "Unusually long URL (over 100 characters).":
        "Long URLs can make it harder to notice the actual destination.",

    "Uses an IP address instead of a familiar domain.":
        "An IP address instead of a domain name deserves closer inspection.",

    "Contains many hostname segments/subdomains.":
        "Multiple hostname segments can make a domain look more official than it is.",

    "Contains a punycode-style hostname.":
        "Punycode can represent characters that resemble familiar letters.",

    "Uses HTTP. HTTPS alone does not prove trust.":
        "HTTP does not encrypt the connection, but HTTPS alone does not prove legitimacy."
}


def inspect_url(raw_url):
    """Check URL text for selected phishing warning signs."""

    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    # Handle malformed URL input
    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    # Check 1: @ symbol
    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    # Check 2: URL length
    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    # Check 3: IP address hostname
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    # Check 4: Number of hostname segments
    labels = [part for part in host.split(".") if part]

    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    # Check 5: Punycode marker
    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    # Check 6: HTTP scheme
    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    return findings


def display_results(findings):
    """Display warnings, explanations and an overall summary."""

    if not findings:
        print("\nNo listed warning signs found.")
        print("This does NOT prove that the URL is safe.")
        return

    print("\n--- URL ANALYSIS RESULTS ---")

    for number, warning in enumerate(findings, start=1):
        print(f"\n{number}. {warning}")

        explanation = REASONS.get(warning)

        if explanation:
            print(f"   Why it matters: {explanation}")

    print("\n--- SECURITY SUMMARY ---")
    print(f"Review carefully: {len(findings)} warning sign(s) found.")
    print("Do not trust a URL based only on these checks.")
    print("Verify unexpected links through an independent official source.")


def main():
    print("=" * 50)
    print("       EWB PHISHING URL AWARENESS CHECKER")
    print("=" * 50)
    print("Text-based checks only. No websites are opened.")
    print("Type 'quit' to exit the program.")

    while True:
        raw_url = input("\nEnter a sample URL: ")

        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("\nGoodbye! Stay alert online.")
            break

        findings = inspect_url(raw_url)
        display_results(findings)


if __name__ == "__main__":
    main()
