# 🛡️ XSS Prevention Cheat Sheet

Cross-Site Scripting (XSS) is one of the most common web security issues. It happens when a website includes untrusted input in a page without proper validation or escaping, allowing attackers to run malicious scripts in a user's browser.

---

## 🚨 What is XSS?

XSS lets an attacker inject JavaScript into a page. This can lead to stolen cookies, session hijacking, account takeover, and more. It often shows up in form fields, URLs, or user-generated content.

---

## 🧠 Common Types

- **Stored XSS** – The malicious script is saved on the server (e.g., in comments or profiles).
- **Reflected XSS** – The script is immediately reflected in the page (e.g., in a search result).
- **DOM-based XSS** – JavaScript on the page processes untrusted input from the DOM without validation.

---

## ✅ Prevention Tips

- Always **escape dynamic content** before rendering it:
  - HTML output → escape `<`, `>`, `&`, `"`, `'`
  - JavaScript → avoid injecting values directly into scripts
  - URLs → encode parameters
- Use `textContent` or safe templating instead of `innerHTML`.
- Sanitize HTML input when rich text is required.
- Apply strict input validation (type, length, format).
- Implement a Content Security Policy (CSP) to limit script execution.
- Default to "deny all" and only allow what you explicitly need.

---

## ❌ What to Avoid

- Don’t trust user input — ever.
- Don’t use `innerHTML` or `.insertAdjacentHTML` with raw input.
- Don’t disable escaping in your template engine.
- Don’t let users upload raw HTML or scripts without sanitizing.

---

## 🧪 Example Payloads

Use these to test your forms and inputs:

```html
<script>alert('XSS')</script>
<img src=x onerror=alert(1)>
<svg/onload=alert(1)>
"><script>alert(1)</script>
