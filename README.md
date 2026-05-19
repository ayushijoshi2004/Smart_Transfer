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
- **Multi-provider comparison**: 8+ transfer methods analyzed side-by-side
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

- **Standard mode**: 70% cost, 30% speed
- **Express mode**: 50% cost, 50% speed
- **Same-day mode**: 30% cost, 70% speed

Risk tolerance applies penalties to crypto options:
- Conservative: 40% penalty
- Balanced: 15% penalty
- Flexible: No penalty

## Installation

```bash
git clone [repository-url]
cd wisetransfer
npm install
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