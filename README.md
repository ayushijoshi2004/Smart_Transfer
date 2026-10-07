# SmartTransfer

An intelligent comparison platform for international money transfers. Compare traditional banks, fintech services, and cryptocurrency options to find the optimal route for your transfer.

## Overview

Sending money internationally involves hidden costs and complex tradeoffs. SmartTransfer analyzes multiple transfer methods to show you the true total cost, speed, and risk profile of each option.

**Compares:**
- Traditional banks (wire transfers)
- Fintech platforms (Wise, Remitly, Western Union)
- Digital wallets (PayPal)
- Cryptocurrency rails (USDC on Ethereum, Solana, Polygon)

## Features

### Core Functionality
- **Multi-provider comparison**: Multiple transfer methods analyzed side-by-side
- **Total cost transparency**: Flat fees + percentage fees + FX markups all included
- **Adaptive scoring**: Rankings adjust based on your urgency and risk tolerance
- **Visual analytics**: Charts showing fee breakdowns and value comparisons

### Smart Features
- **Currency normalization**: All transfers converted to USD for fair comparison
- **Real-time FX rates**: Live exchange rates via Frankfurter API
- **Risk indicators**: Tax implications and volatility warnings for crypto
- **Multiple sorting options**: Best match, cheapest, or fastest

## How It Works

1. **User Input**: Amount, origin currency, destination currency, urgency level, risk tolerance
2. **Normalization**: All amounts converted to USD using live rates
3. **Fee Calculation**: Each provider's total cost calculated (fees + FX markup)
4. **Adaptive Scoring**: Providers ranked based on your preferences
5. **Visualization**: Results displayed with interactive charts

### Fee Calculation

**Traditional Providers:**
```
Total Fee = Flat Fee + (Amount × Percentage Fee) + (Amount × FX Markup)
```

**Crypto Providers:**
```
Total Fee = On-ramp Fee + Gas Fee + Exchange Fee + Off-ramp Fee + FX Spread
```

### Scoring Algorithm

Recommendations adapt to your priorities:

- **Standard mode**: cost-only ranking
- **Express mode**: 60% cost, 40% speed
- **Same-day mode**: 30% cost, 70% speed

Risk tolerance applies penalties to crypto options:
- Conservative: 40-point penalty
- Balanced: 15-point penalty
- Flexible: 10-point bonus

## Installation

```bash
git clone https://github.com/ayushijoshi2004/Smart_Transfer.git
cd Smart_Transfer
npm ci
cp .env.example .env.local
npm run dev
```

Open http://localhost:5173

## Tech Stack

- **React 19**: Frontend framework with hooks
- **Vite 7**: Build tool and dev server
- **Recharts 3.7**: Data visualization
- **Frankfurter API**: Exchange rates

## Project Structure

```
src/
├── App.jsx          # Main application component
├── currency.js      # Destination currencies and rate fetching
├── gemini.js        # AI explanation service
├── logo.js          # Logo asset
├── main.jsx         # Entry point
└── index.css        # Global styles
```

## Key Insights

**FX Markups Are Hidden Costs**: Most fees hide in exchange rate spreads, not flat charges. A "free" transfer with 3% FX markup costs more than a $10 transfer with 0.5% markup.

**Speed vs Cost Tradeoffs**: Sometimes waiting saves significantly. Other times, speed is worth the premium. Context matters.

**Crypto Viability**: Fast (30 min) and cheap on Solana/Polygon, but comes with tax implications and technical complexity.

## Use Cases

- International students sending money home
- Remote workers receiving payments across borders
- Families supporting relatives abroad
- Businesses making cross-border transactions
- Comparing crypto vs traditional transfer methods

## Contributing

Contributions welcome. Areas for improvement:
- Additional provider integrations
- Corridor-specific optimizations
- Historical rate tracking
- Mobile responsiveness improvements

## Acknowledgments

- Frankfurter API for exchange rate data
- Recharts for visualization components
- Built for HackHers 2026
## Prototype boundaries

Provider fees, settlement estimates and risk penalties are illustrative constants, not live provider quotes. Origin and destination exchange rates are fetched together from Frankfurter. Unsupported currency pairs disable comparison with an explanatory message. Rankings are a rule-based heuristic, not an ML prediction. Confirm quotes with providers before acting. FX markup/spread is included once in total fees; received funds use the remaining USD amount times the mid-market destination rate.

Optional AI explanations use `VITE_AI_REVIEW_URL`, a server endpoint you supply. A local FastAPI gateway is included in `backend/`; it keeps the Gemini key private and accepts comparison JSON, returning `{ "answer": "..." }`. With no endpoint configured, comparisons still work and the AI panel shows a clear unavailable message. No Gemini key should be set in frontend environment variables.

Run `npm test` for calculation regression checks and `npm run build` for a production build.

### Optional AI server

From `backend/`, create/activate a virtual environment, install `requirements.txt`, and copy `.env.example` to `.env`. Set your private `GEMINI_API_KEY`, then run `uvicorn app:app --host 127.0.0.1 --port 8001`. In the frontend `.env.local`, set `VITE_AI_REVIEW_URL=http://localhost:8001/api/review` and restart Vite. The server allows the local frontend origins only; for deployment, set `FRONTEND_ORIGIN` and provide your own authentication/rate limits.
