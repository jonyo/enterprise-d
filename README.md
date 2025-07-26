# enterprise-d

Circuit Python code for my Enterprise D model

## Progress

### Stardrive

- [x] black primer 1st coat
- [x] Figure out wiring and pre-wire before filling cracks to ensure wire paths are not blocked
- [x] fill cracks with putty
  - [ ] Sand
  - [ ] black primer coat
- [ ] black primer 2nd coat
- [ ] gray primer 1st coat
- [ ] Paint final colors
- [ ] Paint details
- [ ] Wire up all LED at same time on breadboard to test
- [ ] Try out LED backlight for lights - see if it will work
- [ ] Figure out LEDs for blinky lights
- [ ] Figure out deflector dish LED
- [ ] Figure out electronics mounting in the cavity - solution to easy turn on / off power

### Nacelle / Bussard Collector

- [ ] Electronics - test plugging in electronics for both sides
- [x] solder neopixels for bussard collector - Port
- [x] solder neopixels for bussard collector - Starboard
- [ ] Figure out solution for isolated neopixels
- [ ] Figure out way to connect without permanently gluing
- [ ] Re-Print the Nacelle light covers (originals didn't fit)
- [ ] Wire up nacelle and bussard collector - Port
- [ ] Wire up nacelle and bussard collector - Starboard
- [ ] Tint buzzard collector covers - black when off - dip maybe?
- [ ] Nacelle covers - copper when off?
- [ ] black primer - 1st coat
- [ ] touch up cracks if any
- [ ] black primer - 2nd coat
- [ ] Final paint
- [ ] paint details

### Saucer

- [ ] Plan out electronics
  - [ ] Can it use bluetooth to sync with main body?
  - [ ] Probably just LED's for most part
  - [ ] Separate controller and battery?
- [ ] black primer 1st coat
- [ ] Figure out wiring and pre-wire before filling cracks to ensure wire paths are not blocked
- [ ] fill cracks with putty
  - [ ] Sand
  - [ ] black primer coat
- [ ] black primer 2nd coat
- [ ] gray primer 1st coat
- [ ] Paint final colors
- [ ] Paint details

## Updating Circuitpython

Instructions: https://learn.adafruit.com/adafruit-feather-rp2040-pico/circuitpython

## Bundled libraries

In the RP serial monitor consol thingy, use:

```python
help('modules')
```

## Update the Board

Run:

```zsh
cp code.py /Volumes/CIRCUITPY/
```

## noods

https://learn.adafruit.com/noods-uberguide/electrical-properties-2

## LED Driver - AW9523

https://learn.adafruit.com/adafruit-aw9523-gpio-expander-and-led-driver

## neopixels

## lib source

Locally, used `uv` for package management.

## Nacelle and Bussard Scoops

### Wires from Boards to Nacelle

Wiring to each Nacelle, these are wires going from the main body to the Nacelle.

| Source Board | PIN         | Wire Color | To                                           |
| ------------ | ----------- | ---------- | -------------------------------------------- |
| RP2040       | 3.3v        | ?          | -> noods #1<br>-> noods #2<br>-> Bussard PCB |
| RP2040       | GRD         | ?          | -> Bussard PCB                               |
| RP2040       | A0 (GPIO26) | ?          | -> Bussard PCB                               |
| AW9523       | LED_PIN1    | ?          | -> noods #1<br>-> noods #2                   |

### Part Wiring

#### Noods

Wired in parallel, each one:

| Input Wire | Connected To                                     |
| ---------- | ------------------------------------------------ |
| LED_PIN1   | Cathode - (solid side) -> black jump wire        |
| 3.3v       | Anode + (side with - cutout) -> yellow jump wire |

#### Bussard Scoop

| Input Wire | Connected To | Connector Wire on Part |
| ---------- | ------------ | ---------------------- |
| 3.3V       | 3.3V Input   | red                    |
| GRD        | GRD Input    | white                  |
| A0         | D-IN         | yellow                 |

## References

https://forums.adafruit.com/viewtopic.php?t=210325
