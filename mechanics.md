---
layout: page
title: Pictochat
background: grey
---

<div class="col-lg-12 text-center">
	<h2 class="section-heading text-uppercase">Mechanic Changes</h2>
</div>

# General Mechanics

- Ground to air momentum is now preserved whenever you enter jump squat or run off the ledge/platform
- Untechable threshold increased (might be able to make it so they don't happen below 100%, but probably can't)
- Platforms can now be passed through during dash and run states
- Parries can be cancelled with a dash on their first actionable frame
- Parries force the attacking player into a rebound animation, its length depends on the strength of the move
- Parries can reflect projectiles for 50% of their normal strength
- Drift DI from being ledge robbed is removed during the inactionable frames, after which you can drift with 50% acceleration
- Burries and Grabs can now be mashed out by holding either jump or attack. Mashing is still the optimal method, but now it's less binary than "Either mash or don't". Save your controllers!


# Landing Hits

<video src="assets/img/videos/nair.mp4" max-width="1280px" controls></video>

Drag-down aerials have a new mechanic regarding landing hitboxes: the landing hitbox can only activate during the frames of the multihit hitboxes. This means landing before the first frame of the move, or after (or on) the launching hitbox will not spawn the landing hitbox.
