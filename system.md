# HelloCall System Documentation

This file documents the system-related features of the HelloCall app.

## Features

- **System Dialer Simulation**
  - Simulates phone calls without accessing the real device dialer
  - Call logs are stored in Firebase Realtime Database
- **Internal Storage**
  - Stores call logs in internal storage (E: drive simulation)
  - Safe and isolated from other apps
- **Network**
  - Can simulate Wi-Fi connection for testing purposes
  - Documented in `storage.json`
- **Launcher Integration**
  - Can be launched from a custom Android launcher (documentation in `create_android_launcher.md` / `.html`)

## Notes

- All features are **simulated and safe**
- No real phone calls or sensitive data are accessed
- Fully compatible with documentation on GitHub
