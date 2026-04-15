#!/usr/bin/env python3
"""
Run this in your hivemind-agency.github.io folder:
  python3 patch_index.py

It reads index.html, applies all updates, and saves index.html
"""
import sys, os

CHANGES = [
    ("Atlas is live and answering customers right now",
     "Atlas Voice AI is live \u2014 answering calls &amp; texts 24/7"),

    ("Atlas by HiveMind AI handles your leads, support, bookings, and social media 24/7 \u2014 so you can focus on the work, not the phone.",
     "Atlas by HiveMind AI answers your calls in under a second, handles texts 24/7, qualifies leads, books appointments, and creates social content \u2014 so you never miss a customer again."),

    ("Trusted by businesses across Minnesota",
     "64/64 scenarios tested &middot; Live in production"),

    (">See How It Works<", ">See Voice Demo<"),

    ('"Live Demo"', '"Voice + SMS"'),

    ("See Atlas handle a<br><em>real conversation</em>",
     "Voice AI answers calls.<br><em>SMS handles the rest.</em>"),

    ("A new patient books an appointment at 7:42 PM on a Tuesday \u2014 captured, qualified, and scheduled in under 2 minutes.",
     "A roofing contractor calls after hours. Your phone rings first \u2014 if you don't answer, Atlas picks up in under a second and handles the entire conversation naturally."),

    ("Responds in under 15 seconds", "Answers calls in under 1 second"),
    ("Every time. Every day. Every industry.", "Voice calls answered. Texts handled. Every industry."),

    ("<span>&lt;</span>15<span>s</span>", "<span>&lt;</span>1<span>s</span>"),
    ("Average Response Time", "Voice &amp; SMS Response"),

    ("Atlas responds to every message in under 15 seconds \u2014 24 hours a day, 7 days a week, including holidays.",
     "Atlas answers voice calls in under 1 second via Retell AI, and responds to texts in under 15 seconds \u2014 24/7 including holidays."),

    # Pricing — order matters: Premium first, then Growth, then Starter
    ("<sup>$</sup>3,500<sub>/mo</sub>", "<sup>$</sup>1,800<sub>/mo</sub>"),
    ("<sup>$</sup>1,800<sub>/mo</sub>", "<sup>$</sup>1,200<sub>/mo</sub>"),
    ("<sup>$</sup>800<sub>/mo</sub>",  "<sup>$</sup>600<sub>/mo</sub>"),

    # Plan features
    ("<li>1 AI Agent of your choice</li><li>SMS integration</li>",
     "<li>Voice AI answering (ring-then-Atlas)</li><li>1 AI Agent of your choice</li><li>SMS integration</li>"),

    ("<li>All 4 AI Agents</li><li>SMS + CRM integration</li>",
     "<li>Voice AI + All 4 SMS Agents</li><li>SMS + CRM integration</li>"),

    # How it works step 3
    ("We text-enable your existing number \u2014 landline or cell. Calls work exactly as before. Atlas handles all texts automatically. Your customers notice nothing different.",
     "We connect your existing number. Calls ring your phone first \u2014 if you're busy, Atlas answers in under a second. Texts are handled automatically. Your customers get a response every time, day or night."),
]

VOICE_CARD = (
    '<div class="bento-card" style="background:linear-gradient(135deg,#0f0f0f 0%,#1a1a2e 100%);'
    'border-color:#2a2a4a;grid-column:span 4;border-radius:var(--radius-lg);padding:1.75rem;">'
    '<div class="agent-tag" style="background:rgba(255,255,255,0.1);border-color:rgba(255,255,255,0.15);'
    'color:rgba(255,255,255,0.6);">00 &middot; Voice AI</div>'
    '<div style="display:flex;align-items:center;gap:1.5rem;flex-wrap:wrap;">'
    '<div class="bento-icon dark" style="background:rgba(99,102,241,0.2);flex-shrink:0;font-size:1.5rem;">&#127897;</div>'
    '<div style="flex:1;min-width:200px;">'
    '<h3 style="color:white;font-size:1.1rem;margin-bottom:0.5rem;">Voice AI \u2014 Answers Calls Like a Human</h3>'
    '<p style="color:rgba(255,255,255,0.6);margin:0;font-size:0.85rem;line-height:1.6;">'
    'Your phone rings first. If you don\'t answer, Atlas picks up in under a second \u2014 qualifies leads, '
    'books demos, handles support. Powered by Retell AI with sub-500ms latency. Sounds like a real person.'
    '</p></div>'
    '<div style="display:flex;gap:2rem;flex-shrink:0;">'
    '<div style="text-align:center;">'
    '<div style="font-size:1.8rem;font-weight:300;color:white;line-height:1;">&lt;1s</div>'
    '<div style="font-size:0.65rem;color:rgba(255,255,255,0.4);letter-spacing:0.06em;text-transform:uppercase;margin-top:4px;">Response</div>'
    '</div>'
    '<div style="text-align:center;">'
    '<div style="font-size:1.8rem;font-weight:300;color:white;line-height:1;">24/7</div>'
    '<div style="font-size:0.65rem;color:rgba(255,255,255,0.4);letter-spacing:0.06em;text-transform:uppercase;margin-top:4px;">Always on</div>'
    '</div>'
    '<div style="text-align:center;">'
    '<div style="font-size:1.8rem;font-weight:300;color:white;line-height:1;">100%</div>'
    '<div style="font-size:0.65rem;color:rgba(255,255,255,0.4);letter-spacing:0.06em;text-transform:uppercase;margin-top:4px;">Captured</div>'
    '</div>'
    '</div></div></div>\n        '
)

SDR_MARKER = '<div class="bento-card featured reveal reveal-delay-1">'

def patch(html):
    applied = 0
    skipped = []

    # Insert Voice AI card before SDR card
    if SDR_MARKER in html and 'Voice AI' not in html:
        html = html.replace(SDR_MARKER, VOICE_CARD + SDR_MARKER, 1)
        print("  \u2705 Inserted Voice AI bento card")
        applied += 1

    for old, new in CHANGES:
        if old in html:
            html = html.replace(old, new, 1)
            print(f"  \u2705 {old[:60]}...")
            applied += 1
        else:
            skipped.append(old[:60])

    print(f"\nApplied {applied} changes")
    if skipped:
        print(f"Skipped {len(skipped)} (not found \u2014 may already be updated):")
        for s in skipped:
            print(f"  \u26a0\ufe0f  {s}...")

    return html


if __name__ == "__main__":
    path = "index.html"
    if not os.path.exists(path):
        print(f"Error: {path} not found. Run this from your website folder.")
        sys.exit(1)

    print(f"Reading {path}...")
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    print("Applying changes...\n")
    updated = patch(original)

    # Backup original
    backup = "index_backup.html"
    with open(backup, "w", encoding="utf-8") as f:
        f.write(original)
    print(f"\nBackup saved to {backup}")

    # Write updated
    with open(path, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"Updated {path} saved")
    print("\nDone! Review index.html then push to GitHub.")
