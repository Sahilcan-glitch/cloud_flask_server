# Cloud Flask Class Server 🌐

A minimal **Flask API** for classroom projects in **Embedded AI & Robotics / Data Science**.

https://cloud-flask-server.onrender.com

This server runs in the **cloud** (e.g. on Render) and provides a shared endpoint where all student groups can:

- Send log entries (sensor values, events, statuses, etc.)
- Retrieve all logs or filter by group

Designed to be simple enough for beginners, but realistic enough to feel like a real backend.

---

## 1. Features

- ✅ Simple **REST API** with JSON
- ✅ Central log store for all groups
- ✅ `POST /log` to send data
- ✅ `GET /log` to see everything
- ✅ `GET /log/<group_id>` to filter per group
- ✅ Works with Python, Colab, Streamlit, and IoT boards (ESP32, Uno WiFi, etc.)

> Note: This version stores data **in memory**, so data resets when the server restarts (good enough for class demos).

---

## 2. API Overview

### Base URL

When deployed (e.g. on Render), you’ll get a URL like:

```text
https://cloud-flask-server.onrender.com
