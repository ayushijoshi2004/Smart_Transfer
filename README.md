# SmartTransfer

**Compare modeled international money-transfer options by cost, speed and risk preference.** Enter an amount and currency pair, then explore bank, remittance, wallet and cryptocurrency routes side by side.

SmartTransfer is a HackHers 2026 comparison prototype. Exchange rates come from Frankfurter; provider fees, settlement times and risk scores are illustrative constants, not live provider quotes. The app does not send money.

## What the app does

- Converts the source amount to USD to compare routes on a common basis.
- Calculates modeled fees, FX markup and estimated destination funds.
- Ranks routes using urgency and risk preferences, with sorting by match, cost or time.
- Visualizes comparisons and fee breakdowns through interactive charts.
- Optionally requests a concise Gemini explanation through a server-side API gateway.

Bank/remittance routes combine flat fees, percentage fees and FX markup. Crypto routes model on/off-ramp costs, gas, trading fees and spread. FX spread is deducted once; destination funds use the remaining amount and the mid-market rate. Rankings are deterministic heuristics, not machine-learning predictions.

## Tech stack

| Layer | Technologies |
| --- | --- |
| Interface | React 19, JavaScript, CSS |
| Tooling / charts | Vite 7, Recharts 3 |
| Exchange-rate data | Frankfurter API |
| Optional AI gateway | Python, FastAPI, Uvicorn, Requests, python-dotenv |
| Optional model | Gemini REST API (`gemini-2.5-flash` in the gateway) |
| Checks | Node test runner, ESLint, Vite build |

```text
Browser → Frankfurter exchange rates
        → local fee/ranking calculations → comparison charts
        → optional FastAPI gateway → Gemini explanation
```

## Run locally

Use Node.js 22.12+ (or another Vite 7-compatible release).

```sh
git clone https://github.com/ayushijoshi2004/Smart_Transfer.git
cd Smart_Transfer
npm ci
cp .env.example .env.local
npm run dev
```

Open `http://localhost:5173`. Comparisons work without the AI gateway. Unsupported exchange-rate pairs disable comparison with an explanatory message.

### Optional AI explanations

In a separate terminal, from the repository root:

```sh
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
# Set GEMINI_API_KEY privately in backend/.env.
uvicorn app:app --host 127.0.0.1 --port 8001
```

Set this public endpoint in the frontend `.env.local`, then restart Vite:

```dotenv
VITE_AI_REVIEW_URL=http://localhost:8001/api/review
```

Only the URL belongs in browser configuration. The Gemini key stays in the backend. Without a configured endpoint/key, the app reports that explanations are unavailable. Set `FRONTEND_ORIGIN` on the gateway for your frontend origin; the included defaults are for local development.

## Checks

```sh
npm test
npm run lint
npm run build
```

The existing calculation tests cover double-counted FX markup and non-negative received funds. They do not validate current provider prices or the complete ranking pipeline. Lint currently reports existing formatting and component issues; see the repository review before treating it as a passing quality gate.

## Project layout

- `src/App.jsx`: interface, illustrative provider catalog, fee/ranking logic and charts.
- `src/calculations.js`: received-funds calculation.
- `src/currency.js`: supported destination-currency metadata.
- `src/gemini.js`: optional explanation-endpoint client.
- `backend/app.py`: server-side Gemini gateway.
- `tests/`: calculation regression tests.

## What needs work next

Move provider pricing, fee calculations and scoring out of the large UI component; test them independently. Add quote timestamps/provenance if real provider integrations are introduced. Expand tests for currency failures, urgency/risk ranking and the AI gateway. Clean up lint failures and add screenshots plus a sample comparison for demonstrations. A public AI endpoint also needs authentication and rate limits.

Built with Frankfurter and Recharts for HackHers 2026.
