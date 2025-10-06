# AI Dev Notes

This file logs prompts used with ChatGPT 

## Prompts

1) Build responsive site header + sticky nav
Prompt: "Create a semantic, responsive header with a sticky top nav using Inter font and a simple brand link on the left, links on the right."
AI Output:Provided `header.navbar` HTML/CSS with sticky positioning and flex layout.
Action:Accepted with minor edits to match color tokens and link spacing.

2) Accessible contact form with client-side validation
Prompt: "Write an accessible contact form with First/Last name, Email (pattern), Password + Confirm Password (minlength 8) and a JS validator that shows inline error and prevents submit."
AI Output:Generated HTML with labels/for, `required`, `pattern`, and a basic JS validation snippet.
Action: Modified to add `aria-live` error region, `.error` styles, and redirect to `thankyou.html` on success.

3) About page content block
Prompt: "Draft a friendly, professional About section that mentions acrylic painting since middle school and love for movies."
AI Output: A 2‑paragraph bio and bullet list for hobbies.
Action: Accepted with wording tweaks to fit tone and length.

#150‑Word Reflection

Using AI sped up scaffolding—especially repetitive layout (header/footer), responsive grids, and form validation patterns. It also helped me remember HTML and accessibility attributes like `label for/id` wiring. However, AI sometimes proposed non‑semantic wrappers or overly generic CSS names that could conflict, so I standardized tokens and simplified selectors. For validation, AI suggested complex frameworks, but I kept plain JavaScript to meet the assignment and avoid dependencies. I verified everything manually in two browsers and adjusted spacing and contrast for readability. Overall, I used AI to accelerate boilerplate and idea generation while keeping full control over content, styling, and final code quality.
