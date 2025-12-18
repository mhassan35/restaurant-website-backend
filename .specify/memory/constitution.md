Below is a **fully updated, concrete, and usable Constitution** for your **Restaurant Website (Frontend + FastAPI Backend + Vercel)** project.
All placeholders have been removed, and everything is **explicitly specified** so this file can actually guide development and avoid confusion later.

You can copy-paste this directly as `CONSTITUTION.md`.

---

# Restaurant Website System Constitution

## Core Principles

### I. API-First Architecture

All data must originate from the backend API.

* Frontend **must not** contain hardcoded business data (e.g., menu items).
* Backend is the single source of truth for:

  * Menu items
  * Images (URLs)
  * Categories
  * Ratings and prices
* Any UI feature must be backed by an API endpoint before implementation.

---

### II. Clear Frontend–Backend Contract

Strict contract enforcement between frontend and backend.

* Backend responses **must match** defined schemas.
* Frontend TypeScript types **must mirror** backend response models.
* Breaking API changes require:

  * Version bump
  * Frontend update
  * Documentation update

Example contract:

```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "price": number,
  "image": "absolute_url",
  "category": "string",
  "rating": number
}
```

---

### III. Static Assets Ownership

Clear ownership rules for images and static files.

* **Backend owns all dynamic images**

  * Menu images
  * Food images
* Images must be served via:

  ```
  /static/images/<filename>
  ```
* Frontend must **never assume relative image paths**.
* All image URLs stored in database must be **absolute URLs**.

Example:

```
https://restaurant-website-backend-blond.vercel.app/static/images/pasta.png
```

---

### IV. CORS & Environment Safety (NON-NEGOTIABLE)

Cross-origin rules must be explicit and minimal.

* Allowed origins:

  * `http://localhost:3000`
  * Production frontend Vercel domain
* Wildcard (`*`) origins are **not allowed** in production.
* Environment variables must be used for:

  * Database URL
  * API base URLs
  * Deployment-specific configs

---

### V. Deployment Discipline

Deployment behavior must be predictable and reproducible.

#### Backend (FastAPI)

* Deployed on **Vercel**
* Entry point:

  ```
  app/main.py
  ```
* Static files mounted explicitly:

  ```python
  app.mount("/static", StaticFiles(directory="app/static"), name="static")
  ```

#### Frontend (Next.js)

* Uses environment variable:

  ```
  NEXT_PUBLIC_API_BASE_URL
  ```
* No hardcoded backend URLs inside components.

---

### VI. Type Safety First

Type safety is mandatory.

* No `any` types in frontend.
* All API responses must be typed.
* Custom hooks (e.g. `useMenuItems`) must return typed objects:

  ```ts
  {
    menuItems: MenuItem[];
    loading: boolean;
    error: string | null;
  }
  ```

---

### VII. Simplicity & Maintainability

Avoid unnecessary complexity.

* No premature abstractions.
* One responsibility per file.
* Clear naming over clever naming.
* If a feature can be explained in fewer files, reduce it.

---

## Technology Stack

### Backend

* FastAPI
* SQLAlchemy
* PostgreSQL (or SQLite for local dev)
* Pydantic
* Python 3.11+

### Frontend

* Next.js (App Router)
* TypeScript
* Tailwind CSS
* Native Fetch API
* Next/Image (configured for external domains)

### Deployment

* Vercel (Frontend + Backend)
* `.env` files locally
* Vercel Environment Variables in production

---

## Development Workflow

1. **Backend First**

   * Create model
   * Create schema
   * Create endpoint
   * Test response

2. **Frontend Integration**

   * Update types
   * Consume API via custom hook
   * Render UI

3. **Validation**

   * API tested via browser / Postman
   * Images load correctly
   * No CORS errors
   * No TypeScript errors

---

## Quality Gates

A feature is **NOT complete** unless:

* Backend endpoint works on Vercel
* Frontend fetches real API data
* Images load from backend `/static`
* No console errors
* No TypeScript warnings
* No hardcoded mock data remains

---

## Governance

* This constitution **overrides all ad-hoc decisions**.
* Any deviation must be:

  * Documented
  * Justified
  * Approved
* Changes require:

  * Version bump
  * Reason for change
  * Migration notes

---

**Version**: 1.0.0
**Ratified**: 2025-12-18
**Last Amended**: 2025-12-18

---

If you want, next I can:

* Align this constitution **exactly** with your current repo structure
* Create a **README.md** based on this
* Or generate a **backend API contract document** for frontend devs
