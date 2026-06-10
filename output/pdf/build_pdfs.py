#!/usr/bin/env python3
"""Render Viet Bui's tailored resumes as one-page PDFs (reportlab platypus)."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

INK = HexColor("#1a1a1a")
GREY = HexColor("#555555")

s_name = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=18, leading=21, textColor=INK, spaceAfter=2)
s_contact = ParagraphStyle("contact", fontName="Helvetica", fontSize=8.5, leading=11, textColor=GREY, spaceAfter=8)
s_h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=INK, spaceBefore=10, spaceAfter=1)
s_role = ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=10, leading=12.5, textColor=INK, spaceBefore=6, spaceAfter=0)
s_meta = ParagraphStyle("meta", fontName="Helvetica-Oblique", fontSize=8.5, leading=10.5, textColor=GREY, spaceAfter=2)
s_body = ParagraphStyle("body", fontName="Helvetica", fontSize=9.3, leading=12.2, textColor=INK, spaceAfter=2)
s_bullet = ParagraphStyle("bullet", parent=s_body, leftIndent=12, bulletIndent=2, spaceAfter=2)

CONTACT = "Gaithersburg, MD &nbsp;•&nbsp; 202.817.6601 &nbsp;•&nbsp; Viet.Bui3@Gmail.com &nbsp;•&nbsp; linkedin.com/in/vietqbui"

def section(story, title):
    story.append(Paragraph(title.upper(), s_h2))
    story.append(HRFlowable(width="100%", thickness=1.1, color=INK, spaceBefore=1, spaceAfter=4))

def bullets(story, items):
    for it in items:
        story.append(Paragraph(it, s_bullet, bulletText="•"))

def build(filename, summary, bobos_title, bobos_bullets, salon_bullets, prior, extra_sections, skills):
    doc = SimpleDocTemplate(filename, pagesize=letter,
                            leftMargin=1.7*cm, rightMargin=1.7*cm,
                            topMargin=1.4*cm, bottomMargin=1.3*cm,
                            title="Viet Bui — Resume", author="Viet Bui")
    st = []
    st.append(Paragraph("VIET BUI", s_name))
    st.append(Paragraph(CONTACT, s_contact))
    section(st, "Summary")
    st.append(Paragraph(summary, s_body))
    section(st, "Experience")
    st.append(Paragraph(f"Bobos of War — {bobos_title}", s_role))
    st.append(Paragraph("Remote / Web3 • 2020 – 2024", s_meta))
    bullets(st, bobos_bullets)
    st.append(Paragraph("Bethesda Salon — Co-Owner", s_role))
    st.append(Paragraph("Bethesda, MD • 2014 – 2020", s_meta))
    bullets(st, salon_bullets)
    section(st, "Prior Experience")
    st.append(Paragraph(prior, s_body))
    for title, paras in extra_sections:
        section(st, title)
        for p in paras:
            st.append(Paragraph(p, s_body))
    section(st, "Core Skills")
    if isinstance(skills, list):
        bullets(st, skills)
    else:
        st.append(Paragraph(skills, s_body))
    doc.build(st)
    print("built", filename)

PRIOR_BD = ("<b>Hospitality &amp; Culinary (2012 – 2020):</b> Executive Chef at Driftwood Kitchen (DC) — promoted from "
            "Line Cook in 10 months. Front-of-house and kitchen roles in NYC and DC built the customer-facing communication "
            "and operating-under-pressure muscle that carries into high-volume BD work.")

build("Viet_Bui_Resume_Immutable.pdf",
    summary=("Crypto-native BD operator with 4+ years in Web3 and a deep network across NFT and token projects. "
             "Co-founded an NFT project that raised over $2M through community-led GTM and personally sourced, negotiated, "
             "and closed partnerships with 40+ projects across the ecosystem. Looking to convert a 40-deal Web3 partnerships "
             "track record into ecosystem BD for web3 gaming."),
    bobos_title="Co-Founder &amp; Partnerships Lead",
    bobos_bullets=[
        "Sourced, pitched, and closed partnerships with 40+ crypto and NFT projects — many gaming-adjacent communities — running an inbound + outbound BD motion across Discord, Twitter, and direct founder outreach.",
        "Co-founded an NFT project that raised over $2M through a community-led go-to-market strategy; owned the full funnel from lead-gen to close.",
        "Built and maintained direct relationships with founders, core teams, and community leads across the Web3 ecosystem — a live partner network for ecosystem BD.",
        "Created the Bobo Olympics: a gaming-style, multi-week community competition I productized and cross-sold to 40+ partner communities. Every event was a deal — pitched, negotiated terms, coordinated logistics, delivered on schedule.",
        "Moved every signed deal to go-live: coordinated cross-team delivery across art, smart contract dev, marketing, and community ops. Managed a distributed team across time zones; async-native.",
        "Owned treasury and budget allocation; deep fluency in token economics, on-chain activity, and crypto market structure — can talk web3 game-economy design credibly with studios.",
        "Ran my own pipeline and relationship tracking across 40+ active deals for 4 years with a weekly cadence — no CRM budget, no dropped threads.",
    ],
    salon_bullets=[
        "Co-owned and operated two locations with full P&amp;L responsibility for 6 years; grew revenue through pricing, service expansion, and retention programs — owned a number end-to-end before ever carrying a quota.",
        "Managed a team of 11 across hiring, scheduling, payroll, and performance.",
        "Owned vendor relationships, contract negotiation, and inventory across both locations.",
    ],
    prior=PRIOR_BD,
    extra_sections=[],
    skills=[
        "<b>BD &amp; Partnerships:</b> deal sourcing, pitching, negotiating, closing, founder relationship management, partner GTM, pipeline management, cross-functional delivery to go-live.",
        "<b>Crypto / Web3:</b> NFT markets and web3 gaming-adjacent ecosystems, token launches, tokenomics, EVM / L2 landscape, Discord &amp; Twitter community ops.",
        "<b>Operations:</b> cross-functional coordination, async distributed-team management, treasury and budget ownership.",
    ])

build("Viet_Bui_Resume_Base.pdf",
    summary=("Crypto-native operator who grew an NFT community to a $2M raise through Twitter/Discord-first GTM. "
             "Four years living on crypto Twitter through a full market cycle: founder-voice content, partner co-announcements, "
             "Spaces, and weekly community programming. Looking to bring that channel instinct to the voice of Base."),
    bobos_title="Co-Founder &amp; Community/Partnerships Lead",
    bobos_bullets=[
        "Ran the project's X/Twitter and Discord presence from zero audience; community-led GTM produced a $2M+ raise with no paid media.",
        "Built reach through ecosystem amplification: closed 40+ partnerships with crypto and NFT projects via founder-direct DMs, turning each into co-announcements, joint Spaces, and cross-community campaigns — every deal was a reach multiplier.",
        "Produced the Bobo Olympics: recurring weekly content programming — a multi-week, multi-project community competition that sustained engagement for months, co-marketed by every partner community.",
        "Held the community together through the 2022 drawdown with transparent treasury updates, AMAs, and consistent posting cadence — comms under FUD, not just in a bull market.",
        "Shipped content weekly across a distributed team (art, dev, marketing, community) in multiple time zones: clear briefs, written decisions, zero missed weeks during the series.",
        "Deep fluency in EVM ecosystems, token economics, and on-chain culture — can write for builders without a glossary.",
    ],
    salon_bullets=[
        "Co-owned two locations for 6 years with full P&amp;L; built retention programs and customer communication systems — audience care before it was called community management.",
        "Managed a team of 11; ran scheduling, vendor relationships, and operations with checklist-level attention to detail — the same muscle as running an always-on social channel.",
    ],
    prior=("<b>Hospitality &amp; Culinary (2012 – 2020):</b> Executive Chef at Driftwood Kitchen (DC) — promoted from "
           "Line Cook in 10 months. High-volume, customer-facing work under pressure."),
    extra_sections=[],
    skills=[
        "<b>Social &amp; Community:</b> X/Twitter growth, Discord ops, content calendars, Twitter Spaces, AMAs, partner co-marketing, community escalation/FUD response, social analytics.",
        "<b>Crypto / Web3:</b> EVM / L2 ecosystems, NFT markets, token launches, tokenomics, crypto Twitter culture.",
        "<b>Production:</b> async cross-functional coordination, weekly programming cadence, brief-driven delivery.",
    ])

build("Viet_Bui_Resume_FunctionHealth.pdf",
    summary=("Founder-operator with 10 years of full-accountability work: 6 years running two businesses end to end "
             "(scheduling, payroll, compliance, vendors, books) and 4 years co-founding a Web3 project where I coordinated "
             "a distributed team across time zones and owned the treasury. I run my own work through AI workflows I set up "
             "and operate myself. Looking to put that operating muscle behind a founder instead of being one."),
    bobos_title="Co-Founder &amp; Partnerships Lead",
    bobos_bullets=[
        "Ran a founder's calendar in practice: managed 40+ active partner relationships on a weekly cadence for 4 years with my own tracking system — no dropped threads.",
        "Coordinated cross-team delivery across art, dev, marketing, and community ops; managed a distributed team across time zones, async-first with written briefs and clear owners.",
        "Owned treasury and budget allocation through a full market cycle; detail-heavy record keeping with real money at stake.",
        "Handled high-volume founder communications across Discord, Twitter, and email — triage, prioritization, and follow-up at speed.",
        "Co-founded the project and helped raise over $2M through community-led GTM.",
    ],
    salon_bullets=[
        "Ran operations for two locations for 6 years: scheduling and payroll for 11 employees, hiring, performance, and conflict resolution.",
        "Owned licensing, compliance, bookkeeping, and financial reporting — deadline-driven administrative work where mistakes cost money.",
        "Managed vendor relationships, contract negotiation, and inventory across both locations.",
        "Full P&amp;L responsibility; grew revenue through pricing, service expansion, and retention programs.",
    ],
    prior=("<b>Hospitality &amp; Culinary (2012 – 2020):</b> Executive Chef at Driftwood Kitchen (DC) — promoted from "
           "Line Cook in 10 months; ran kitchen scheduling, ordering, and service under pressure. Earlier front-of-house "
           "roles built fast, polished, customer-facing communication."),
    extra_sections=[("AI & Tools",
        ["I set up and operate my own AI agent workflows. Current example: an automated job-search pipeline on Claude that "
         "scans ~45 job sources on a schedule, scores roles against my criteria, discards dead listings, drafts documents, "
         "and tracks everything in a ledger — AI drafts, I review and send. Comfortable picking up any scheduling, docs, or "
         "expense stack fast; I learned point-of-sale, payroll, and booking systems as an owner because no one else was going to."])],
    skills=("Calendar &amp; pipeline management • async written communication • payroll/bookkeeping/compliance • "
            "vendor &amp; contract management • event and logistics coordination • AI workflow automation • "
            "discretion with sensitive information (treasury, payroll, licensing)"))
