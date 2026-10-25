# ACPDC: Acoustic Canopy Pest Detection Collar

Vishwakarma Awards 2026-27 · Track: Technological Innovation for Rural Sustainability · Team ID: `TODO`

A clamp-on, solar-powered collar that listens for larval boring inside a tree trunk and sends a LoRa alert for that single tree, so treatment can be targeted instead of blanket spraying.

![How the collar senses a boring larva](docs/images/collar_principle.png)

## How it works

1. **Sense:** boring larvae make impulsive clicks that travel through the wood to a rigid Al-6061 plate with a PZT-5H disc (no rubber in the sensing path).
2. **Condition:** analog front end (TLV9062S, ~30 dB gain, per-band low-pass) feeds the ADC.
3. **Detect:** duty-cycled capture, IIR band-pass, adaptive threshold and N-of-M burst voting.
4. **Alert:** LoRa point-to-point (865–867 MHz) to a receiver and dashboard, with ack + retry. Target: alert within 48 h of onset.

![Signal path and alert path](docs/images/signal_chain.png)
![Orchard network](docs/images/orchard_network.png)

The waveform and orchard images are illustrations, not measured data.

## Open design decisions

- Sensing band: bench-test 1–14 kHz (48 kS/s) vs 20–60 kHz (200 kS/s) before freezing hardware.
- Power: scheduled capture and AFE shutdown to reach the ≤100 µA average target.
- Telemetry: LoRa P2P for the prototype; LoRaWAN gateway deferred.

## Repository layout

| Path | Contents |
| --- | --- |
| `docs/` | Stage 2 submission deck and figures |
| `hardware/cad/` | SolidWorks and `.STEP` files, FEA results |
| `hardware/pcb/` | KiCad project (`.kicad_sch`, layout, DRC log), BOM |
| `firmware/` | STM32WLE5 (Seeed Wio-E5) firmware source |
| `data/` | Bench recordings and test logs |
| `tools/` | Scripts, e.g. `make_illustrations.py` regenerates the figures |

## Roadmap

Nov 2026 fabricate · Dec 2026 assemble and bring up · Jan 2027 integrate · Feb 2027 validate (3-node prototype, laptop receiver, bench and orchard logs).

## License

`TODO`: choose a license before making the repository public.
