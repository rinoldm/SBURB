![SBURB preview image](https://i.imgur.com/3X19LEL.png)

# SpaceX Booster Use/Reuse Beholder (SBURB)

SBURB is a tool developed to provide a nice infographic of the individual timelines of each core, which shows very well the rapid acceleration in launch cadence as well as improvements in core landing and reuse. It was inspired by [this Reddit post](https://www.reddit.com/r/SpaceXLounge/comments/8jmn3e/spacex_recovery_history_preblock_5_graphic/) which presented the same idea, which I immediately loved, but it turned out its author wouldn't update it, so I decided to make my own version that could be updated with new launches and cores easily.

### How to use

You need to have Python 3 and Matplotlib installed.

```sh
py sburb.py [mode]
```

This script only takes one argument, `mode`, which can be `0`, `1`, or `2`.
* `0` shows the launches from all the cores.
* `1` shows the launches from the Falcon 1 cores, the Falcon 9 v1.0 cores (B0001 to B0007) and the Falcon 9 v1.1 cores (B1001 to B1018).
* `2` shows the launches from the Falcon 9 Full Thrust cores (B1019 to the latest core).

I somewhat arbitrarily made this division because "not much" happened in part `1`, as it was still the beginnings of SpaceX followed by the experimental phase of first stage landings, so I find part `2` to be a lot more interesting and exciting as it shows the first successful landings and then a fantastic progress in rapid reuse.

As more cores are built and more launches happen, they can be added simply by adding new entries in the lists of cores and launches in `cores.py` and `launches.py` respectively.

### Known issues

* **Documentation of early cores :** unfortunately, while the events of each launch are easy to verify, the cores used before Falcon 9 Full Thrust (before B1019) are not known with certainty, as they weren't painted on the rocket or otherwise publicized. If you look at any public source, you'll see that most of these cores are marked as "presumed" or just unknown. Therefore, keep in mind that the correspondance between launches and individual cores pre-Full Thrust shown by this tool is only an approximation and may be inaccurate.

* **Hardcoding :** not only was I not very familiar with either Python or Matplotlib, my priority here was to make something that would look pretty as a chart, not elegant code. More particularly, I wanted to have the best result with mode `2` in a maximized window on my screen. As such, most of the visuals are hardcoded so that it looks best in this particular scenario, and other modes and window sizes will most likely look a bit off. This problem concerns : the size of the icons, the size of the font for the core numbers on the left axis and for the number of days in the reuse rectangles, the spacing between the left axis and the core version names, and the width of the Falcon Heavy rectangle. I may or may not try to fix those in the future.