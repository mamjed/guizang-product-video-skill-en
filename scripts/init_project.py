#!/usr/bin/env python3
"""Initialize an isolated promo workspace without installing dependencies or touching the repo."""
import argparse
import json
import shutil
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--style', required=True, choices=['repo', 'default', 'hybrid'])
    parser.add_argument('--repo', type=Path)
    args = parser.parse_args()
    repo = args.repo.expanduser().resolve() if args.repo else None
    target = args.output.expanduser().resolve()
    if args.style in ('repo', 'hybrid') and (repo is None or not repo.is_dir()):
        parser.error('repo/hybrid requires --repo pointing to an existing repository')
    if repo is not None and not repo.is_dir():
        parser.error('--repo must be a directory')
    if target.exists() and (not target.is_dir() or any(target.iterdir())):
        parser.error('output must be absent or empty; existing work is never overwritten')
    skill = Path(__file__).resolve().parents[1]
    if target == skill or skill in target.parents:
        parser.error('output must be outside the skill bundle')
    target.mkdir(parents=True, exist_ok=True)
    shutil.copytree(skill / 'assets/starter', target, dirs_exist_ok=True)
    for name in ['assets', 'evidence', 'renders', 'public']:
        (target/name).mkdir(exist_ok=True)
    if args.style != 'repo':
        shutil.copytree(skill/'assets/fallback', target/'assets/fallback')
        (target/'src/presentations.jsx').write_text("""import React from 'react';
import {CardFrame, CardSurface, FilmButton, FilmBadge} from '../assets/fallback/primitives.jsx';
// Technical fixture using the adapted fallback primitives, not product business components.
export function FeatureVisual() {
  return <CardFrame data-skill-placeholder="true"><CardSurface style={{padding:54}}>
    <FilmBadge>Component Showcase / DEMO</FilmBadge>
    <h2>Components can be plugged right in.</h2>
    <p>Bring in real product components, then arrange selections, expansions, and switches.</p>
    <div style={{display:'flex',gap:16,marginTop:42,fontSize:26}}>
      <FilmButton>Primary action</FilmButton><FilmButton variant="secondary">Secondary action</FilmButton>
    </div>
  </CardSurface></CardFrame>;
}
""")
    shots = [
        {'id':'intro','start':0,'end':3,'type':'title','headlineEn':"What's new",'headline':'What does this update bring?','description':'Explain the change in one sentence first, then show how to use it.'},
        {'id':'component','start':3,'end':7,'type':'detail','headlineEn':'Real components','headline':'Use components straight from the product','description':'Wire in buttons and cards from the repo, then choreograph their entrances and transitions with code.','component':'src/presentations.jsx'},
        {'id':'close','start':7,'end':10,'type':'end','headlineEn':'Ready to share','headline':'Check visuals and audio together','description':'Confirm subtitles can be read and actions can be heard before exporting the video.'},
    ]
    for shot in shots:
        shot.update({'descriptionAt':0,'claim':False,'source':[], 'plainExplanation':shot['description'],
                     'actions':[{'id':shot['id']+'-enter','at':0,'action':'copy enters','soundRequired':False}]})
        shot.setdefault('component', None)
    shots[1]['actions'].append({'id':'component-appear','at':0.45,'action':'controls appear','soundRequired':True})
    shots[2]['actions'][0]['soundRequired']=True
    plan = {'demo':True,'product':'Software Update · Technical Demo','style':args.style,'width':1920,'height':1080,'fps':30,'duration':10,
            'repo':str(repo) if repo else None,'audioRequired':True,'sfxRequired':True,
            'typography':{'mode':'bilingual','zhFont':'PingFang SC / Noto Sans CJK SC','enFont':'Georgia','zhStyle':'sans-serif'},
            'audio':{'ducking':{'enabled':True},'music':{'file':'assets/music.wav','gain':0.65},'cues':[
              {'at':3.45,'actionId':'component-appear','file':'assets/sfx/click.wav','gain':0.8,'role':'sfx','kind':'click'},
              {'at':7.0,'actionId':'close-enter','file':'assets/sfx/ding-dong.wav','gain':0.7,'role':'sfx','kind':'ding-dong'}]},
            'shots':shots}
    (target/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
    (target/'BRIEF.md').write_text(f"""# Video brief

- Status: technical starter, product research and shot list not yet complete.
- Style choice: {args.style} (should come from user-confirmed selection)
- Repo: {repo or 'Not specified, fill in before producing real product content'}
- Product / update scope / release status: to be determined from user input and repo.
- Platform / aspect ratio / duration / language: to be recorded; plan.json is currently a 10-second technical demo only.
- Brand assets / fonts: to be audited.
- Links / CTA allowed: to be recorded per user request.
- Audio: music defaults to code-original; SFX starts with samples suited to this film, filling gaps with skill bundled WAVs only. The technical demo has no audio track yet; the plan lists score and key action SFX separately — they must be actually prepared and mixed in.
- Selling point evidence, style audit, and asset sources: recorded in evidence/.

Preserve existing user decisions; do not pretend unconfirmed fields are confirmed. Sync plan.json with the actual timeline once the production film is complete.
""")
    (target/'DIRECTION.md').write_text('''# Film direction (complete before coding, see references/direction.md)

> This file has only questions, no answers. Each item is derived from the product itself; do not copy the case study or the previous film.

## 1. Reference teardown (write only when the user provided references)
| Technique from the reference | What it expresses | Whether and how this film adapts it |
|---|---|---|

## 2. Product character
- What the product does, who uses it, what it feels like to use:
- Design language (palette, fonts, corner radius, light/dark theme) source:
- Product elements that can become a visual motif (logo geometry, core UI, data shapes, domain metaphors):

## 3. Three directions (spread along different axes)
| Direction | Base color & light | Typography & voice | Motif source | Shot language | Rhythm | Music |
|---|---|---|---|---|---|---|
| A | | | | | | |
| B | | | | | | |
| C | | | | | | |

## 4. Selection & rationale
- Which one, and why it fits this product and audience:
- Film-specific techniques (3–5, each with the product trait it derives from):
- Differences from previous films in this workspace (opening, transitions, backgrounds, score):

## 5. Frame design system
- Aspect ratio / frame rate / base color / safe area:
- Type scale (English, Chinese, description) and font source:
- Product UI on-camera magnification (body text ≥ 22px) and light/dark theme:
- Motion grammar (entrances, camera movement, easing, prohibited items):

## 6. Shot list
| # | Time | Shot | Protagonist | Visuals & actions | Copy | Sound |
|---|---|---|---|---|---|---|
''')
    print(json.dumps({'project':str(target),'style':args.style,'demo':True,'next':'Research the product, then write DIRECTION.md (references/direction.md) before production shots.'},ensure_ascii=False))

if __name__ == '__main__':
    main()
