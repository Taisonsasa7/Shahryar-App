# ShahrayarCore - The Imperial Technical Foundation

## 1. Environment & Architecture
- **Environment:** Node.js (v20+)
- **Hosting:** Replit (Always-on instance)
- **Primary Pattern:** Unified Brain Hub (Event-Driven Architecture)

## 2. Core Service Structure
```text
/src
  /core
    brain.js          // The Unified Brain API (GPT-4o Integration)
    guard.js          // Sovereign Guard Policy (Privacy & Ethics)
  /services
    voice_engine.js   // Affective Interaction Engine (Agora.io + TTS/STT)
    realtime_data.js  // Live API Connectors (Sports, News)
  /bots
    room_bot.js       // Public Room Management (25 Mics Control)
    personal_bot.js   // Private Companion Logic (Memory Sync)
  /api
    routes.js         // External Integrations for Majlis & Store
  index.js            // Main Application Entry Point
```

## 3. Initial Development Task: The Unified Brain API
- **Module:** `src/core/brain.js`
- **Objective:** Establish the connection with OpenAI GPT-4o.
- **Responsibility:** 
  - NLP intent analysis.
  - Sentiment analysis for the Affective Engine.
  - Contextual responses based on user tier and history.

## 4. Implementation Guidelines (The Imperial Guard Policy)
- **72-Hour Rule:** Automatic data purging every 72 hours for absolute privacy.
- **Anti-Expulsion:** Hard-coded logic to prevent arbitrary bans, favoring "Imperial Friendship."
- **Voice Swap:** Dynamic pitch and tone adjustment based on interactor's gender profile.
```,data_type: