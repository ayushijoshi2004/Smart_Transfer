import { test } from 'node:test';
import assert from 'node:assert/strict';
import { calculateReceived } from '../src/calculations.js';
test('FX markup included in total fee is deducted once', () => {
  // $100 principal, $2 FX markup, $3 other fees; 80 destination units/USD.
  assert.equal(calculateReceived(100, 5, 80), 7600);
});
test('fees exceeding principal do not produce negative received funds', () => {
  assert.equal(calculateReceived(1, 5, 80), 0);
});
