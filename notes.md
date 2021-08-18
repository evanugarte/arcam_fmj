## what works
```py
# this toggles power in _write_packet
# src/arcam/fmj/__init__.py:532
data = bytes([
    0x21,
    0x01,
    0x00,
    0x01,
    0x02,
    0x0D
])
print('writing', data)
writer.write(data)
```

## game time
- backtrack from above solution to getting it to work by changing configs
  - modify to_bytes
  - modify actual values defined
- how is state requested?
- get source, volume, power and state to work
- move onto abstracting logic to api
```
GET /health-check, returns power state and volume if on
POST /update, power? volume? source?
```
- website
  - vertical + and - for volume, popup slider in middle of button
  - source dropdown on left
  - power button on top right, enabled or disabled depending on healthcheck
  - use nes.css add to website setup script

## game time but yt control
- [tutorial?](https://0x41.cf/automation/2021/03/02/google-assistant-youtube-smart-tvs.html)
- [obscure repo](https://github.com/mutantmonkey/youtube-remote)
- [pypi bravia control](https://pypi.org/project/bravia-tv/), `play_content`?

### Qs
- can we add a module for the SA10?
