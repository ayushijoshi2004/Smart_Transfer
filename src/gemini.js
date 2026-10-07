// Optional AI gateway: provider credentials belong on your server, never in Vite.
export async function generateAIReview(data) {
  const endpoint = import.meta.env.VITE_AI_REVIEW_URL;
  if (!endpoint) return "AI explanations are not configured. Compare the modeled fees, delivery times, and risk indicators shown here.";
  try {
    const response = await fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    if (!response.ok) throw new Error("AI gateway unavailable");
    const result = await response.json();
    return typeof result.answer === "string" && result.answer.trim()
      ? result.answer : "No explanation is available. Please try again.";
  } catch {
    return "AI explanations are temporarily unavailable. The comparison results are still available.";
  }
}
