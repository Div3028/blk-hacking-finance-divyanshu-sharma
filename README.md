# BlackRock Auto-Saving Retirement Challenge

## Overview

This project implements a production-grade API system for automated retirement savings through expense rounding and investment projection.

The system supports:

- Expense transformation and rounding logic
- Transaction validation
- Temporal constraint validation (q, p, k periods)
- Investment return calculations (NPS and Index Fund)
- Inflation-adjusted projections
- Performance monitoring
- Dockerized deployment

All requirements are implemented strictly according to the challenge specification.

---

## Architecture

- FastAPI (API framework)
- Pydantic (data validation)
- Prefix-sum + binary search interval engine
- O(n log n) complexity
- Docker-based Linux container deployment

---

## Complexity

- Transaction sorting: O(n log n)
- q/p interval application: O((q+p) log n)
- k aggregation: O(k log n)
- Return computation: O(k)

Designed to scale up to 10^6 transactions within practical limits.

---

## Running Locally

### Install dependencies

```bash
pip install -r requirements.txt



### Start the API server

```bashuvicorn main:app --reload
``` 