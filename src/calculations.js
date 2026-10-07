// totalFee includes the FX markup/spread, so apply the mid-market rate once.
export function calculateReceived(amountUSD, totalFee, midMarketRate) {
  return Math.max(0, amountUSD - totalFee) * midMarketRate;
}
