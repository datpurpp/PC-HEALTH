# PC-HEALTH: Visual System State & Forensics Engine

An open-source Python digital forensics and system health analysis suite. This project intercepts raw telemetry signatures and volatile hardware states (RAM heaps, CPU threads, and environment entropy) and maps them into dynamic color arrays. 

By converting complex system metrics into a visual color layout, users can quickly baseline their PC's health and spot hidden background anomalies.

## 📊 The Diagnostic Rule of Thumb
* **Smooth, slow, and steady color movements** = A healthy, optimized PC. The system is handling background tasks efficiently, and memory states are stable.
* **Chaotic, rapid, and aggressive color movement/flashing** = A warning sign. High volatility while the user isn't doing anything indicates that something aggressive (like malware, a crypto-miner, or bloated background spyware) is constantly thrashing the RAM and CPU.

---

## 🛠️ Included Programs

### 1. Static State Capture (Part 1 Base Engine)
Takes a frozen snapshot of volatile memory data at one precise millisecond and maps it to a custom `128x128` pixel grid. Great for capturing a static system baseline.

### 2. Animated Live Feed Engine (Part 2 continuous Output)
Converts your computer's live health metrics into an animated color graph. It pushes a real-time moving color graphics stream to the screen so you can watch background system warfare happen in real-time.

### 3. Full Standard Read Audit (10-Photo Diagnostic Challenge)
Automates the capture of 10 sequential snapshot frames in a row with a built-in time delay. This lets a security analyst scroll through the saved images sequentially to look for sudden visual "jumps" or radical color shifts while the PC is completely idle.

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed, along with the standard imaging library:
```bash
pip install Pillow
```

### Running the Programs
1. Clone the repository or navigate to your downloaded files.
2. Close all active user applications and let your PC sit **idle**.
3. Run any of the tracking scripts inside the `PC-Health-STATECAPTURE` directory:
```bash
python <script_name>.py
```
4. Check the generated `.jpg` outputs or watch the live canvas feed to inspect your system's stability.

---

## 🔧 Open Source Development
This project is built in an **open-source style** meant to be actively developed, modified, and upgraded by the community. 

### Future Upgrade Blueprints
* Implementing 3D volumetric array rendering of telemetry streams.
* Mapping frequency spectrums to continuous moving waveforms.
* Developing algorithmic thresholds to trigger active alert banners on anomalous volatility spikes.
