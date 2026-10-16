import json,colorsys
from pathlib import Path
base=Path(__file__).resolve().parents[1];source=base.parent/'wisteria-blush-theme'
for name in ['themes','assets','store-assets']:(base/name).mkdir(exist_ok=True)
def write(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
rows='''
editor.background tab.activeBackground|FFFCF5|2B3238
foreground editor.foreground terminal.foreground|48515A|E2E5DE
titleBar.activeBackground|E9EDF1|22282D
titleBar.activeForeground|4D5968|CAD2DA
titleBar.inactiveBackground|F0F2F4|1F2429
titleBar.inactiveForeground|88919A|89949D
activityBar.background|DEE5EA|1E252A
activityBar.foreground|5D7288|B8C3D3
activityBar.inactiveForeground|8996A1|7F909C
activityBar.activeBorder|A98599|E1C1D0
sideBar.background|EEF1E8|262D28
sideBar.foreground|54604E|C3CEBD
sideBarSectionHeader.background|E4E9DC|303A30
sideBarSectionHeader.foreground|65715A|D4DDCB
editorGroupHeader.tabsBackground tab.inactiveBackground|ECEFE8|222A2C
tab.inactiveForeground|8B9487|93A18F
tab.activeForeground|566B80|FDECCE
tab.activeBorderTop|B38D9F|E1C1D0
panel.background terminal.background|F5F3EA|252D30
statusBar.background statusBar.noFolderBackground|DCE5D1|354331
statusBar.foreground statusBar.noFolderForeground|536348|DCE7CF
panel.border sideBar.border editorGroup.border tab.border titleBar.border|D8DFD4|414D43
editor.lineHighlightBackground|FBF2DF|343D3F
editor.lineHighlightBorder|EFE6D1|43504C
editorLineNumber.foreground|A3AA9A|788578
editorLineNumber.activeForeground|758466|CEDABF
editorCursor.foreground|71869B|FDECCE
selection.background editor.selectionBackground terminal.selectionBackground|DCE5D0|4D6047
editor.inactiveSelectionBackground|E7EADF|3D4B3A
editor.wordHighlightBackground editor.wordHighlightStrongBackground editor.selectionHighlightBackground|EDF0E180|3B494299
list.activeSelectionBackground|CEDABF|46583F
list.activeSelectionForeground list.inactiveSelectionForeground|46553E|E5ECD9
list.inactiveSelectionBackground|E7EADF|3D4B3A
list.hoverBackground|E5EBDD|333F32
editor.findMatchHighlightBackground|FDECCE|645342
editor.findMatchBackground|EED6AE|826A4C
editor.findMatchBorder|B59A6E|FDECCE
editorBracketMatch.background|E1C1D066|574854
editorBracketMatch.border|AE8E9F|C4A7B7
editorIndentGuide.background1|E5E7DD|404B42
editorIndentGuide.activeBackground1|AFBBA0|7D9172
quickInput.background editorWidget.background editorHoverWidget.background editorSuggestWidget.background notifications.background|FAF9F2|323C38
input.background dropdown.background|FFFEF9|222B27
input.border dropdown.border|CBD4C3|53664C
focusBorder|8CA07C|A9BD96
editorSuggestWidget.selectedBackground|DCE5D0|46583F
editorSuggestWidget.selectedForeground|46553E|E5ECD9
button.background|CEDABF|CEDABF
button.foreground|46553E|2D3C27
button.hoverBackground|BFCEAD|DFE8D2
button.secondaryBackground|E7EBE0|41503A
button.secondaryForeground|647158|DCE7CF
badge.background activityBarBadge.background|71869B|B8C3D3
badge.foreground activityBarBadge.foreground|FFFFFF|2B3238
errorForeground editorError.foreground problemsErrorIcon.foreground|B05E65|E3A4AA
editorWarning.foreground problemsWarningIcon.foreground|9C7B42|E6CCA0
editorInfo.foreground problemsInfoIcon.foreground|567792|B8C3D3
gitDecoration.addedResourceForeground gitDecoration.untrackedResourceForeground editorGutter.addedBackground|70895E|BCD2A8
gitDecoration.modifiedResourceForeground editorGutter.modifiedBackground|A48657|E0C59D
gitDecoration.deletedResourceForeground editorGutter.deletedBackground|B3797E|DDA6AE
diffEditor.insertedTextBackground diffEditor.insertedLineBackground|E8EFDF99|33432F99
diffEditor.removedTextBackground diffEditor.removedLineBackground|F4E3E599|49343A99
'''
palette={'comment':('929B87','91A087'),'keyword,storage':('986A83','E1C1D0'),'string':('647C51','CEDABF'),'entity.name.function,support.function':('567792','B8C3D3'),'entity.name.type,support.type,support.class':('847296','D4C3DF'),'constant.numeric,constant.language,variable.other.constant':('A07845','FDECCE'),'variable':('48515A','E2E5DE'),'variable.parameter':('81785D','D4CDB5'),'variable.other.property,support.variable.property':('54817B','B6D2C7'),'keyword.operator':('78816F','BBC6B2'),'punctuation':('91998A','9FAE9B'),'entity.name.tag':('986A83','EFD1CD'),'entity.other.attribute-name':('A07845','FDECCE')}
def soften(x):
    if isinstance(x,dict):return {k:soften(v) for k,v in x.items()}
    if isinstance(x,list):return [soften(v) for v in x]
    if isinstance(x,str) and x.startswith('#'):
        rgb=[int(x[i:i+2],16)/255 for i in [1,3,5]];h,l,s=colorsys.rgb_to_hls(*rgb)
        if .7<h<.88:
            rgb=colorsys.hls_to_rgb(.24,l,min(s,.23));return '#'+''.join(f'{round(c*255):02X}' for c in rgb)+x[7:]
    return x
m=json.loads((source/'package.json').read_text());m.update(name='harvest-tapestry-theme',displayName='Harvest Tapestry Theme',description='Muted slate blue, sage leaves and pressed-flower pink in coordinated light and dark themes.',keywords=['theme','light','dark','garden','sage','pastel','vintage']);m['galleryBanner']['color']='#2B3238'
for t in m['contributes']['themes']:t['label']=t['label'].replace('Wisteria Blush','Harvest Tapestry');t['path']=t['path'].replace('wisteria-blush','harvest-tapestry')
write(base/'package.json',m)
for i,v in enumerate(['light','dark']):
    t=soften(json.loads((source/'themes'/f'wisteria-blush-{v}-color-theme.json').read_text()));t['name']=f'Harvest Tapestry Theme {v.title()}'
    for row in rows.strip().splitlines():
        keys,l,d=row.split('|')
        for key in keys.split():t['colors'][key]='#'+[l,d][i]
    for rule in t['tokenColors']:
        key=','.join(rule['scope'])
        if key in palette:rule['settings']['foreground']='#'+palette[key][i]
    for key,scope in {'variable':'variable','parameter':'variable.parameter','property':'variable.other.property,support.variable.property','function':'entity.name.function,support.function','method':'entity.name.function,support.function','class':'entity.name.type,support.type,support.class','type':'entity.name.type,support.type,support.class','interface':'entity.name.type,support.type,support.class','variable.readonly':'constant.numeric,constant.language,variable.other.constant'}.items():t['semanticTokenColors'][key]='#'+palette[scope][i]
    write(base/'themes'/f'harvest-tapestry-{v}-color-theme.json',t)
for name in ['LICENSE','CHANGELOG.md','.vscodeignore']:(base/name).write_text((source/name).read_text(encoding='utf-8').replace('Wisteria Blush','Harvest Tapestry'),encoding='utf-8')
for name in ['capture-real-screenshots.py','validate.py']:(base/'scripts'/name).write_text((source/'scripts'/name).read_text(encoding='utf-8').replace('Wisteria Blush','Harvest Tapestry').replace('wisteria-blush','harvest-tapestry'),encoding='utf-8')
demo=base/'scripts/demo-project';demo.mkdir(exist_ok=True)
for p in (source/'scripts/demo-project').iterdir():
    if p.is_file():
        text=p.read_text(encoding='utf-8').replace('Wisteria Blush','Harvest Tapestry').replace('WisteriaBlush','GardenLetter').replace('wisteria violet, dusty blush and peach','slate blue, teal, cream, ochre, brick red and plum').replace('flower-inspired','tapestry-inspired')
        for a,b in [('E0BBE4','B8C3D3'),('957DAD','CEDABF'),('D291BC','E1C1D0'),('FEC8D8','EFD1CD'),('FFDFD3','FDECCE')]:text=text.replace(a,b).replace(a.lower(),b.lower())
        for a,b in [('wisteria:','slate:'),('violet:','sage:'),('blush:','petal:'),('peach:','cream:'),('pink:','peach:'),('.wisteria','.slate'),('.peach','.cream')]:text=text.replace(a,b)
        (demo/p.name).write_text(text,encoding='utf-8')
(base/'README.md').write_text('''# Harvest Tapestry Theme

Muted slate blue, sage leaves and pressed-flower pink in coordinated light and dark themes.

花园来信：奶油信纸、灰蓝墨迹、鼠尾草绿与干花藕粉。

- **Harvest Tapestry Theme Light** — cream paper editor, sage panels and muted rose accents.
- **Harvest Tapestry Theme Dark** — charcoal slate editor, sage panels and pastel syntax colors.

| Region | Light | Dark |
| --- | --- | --- |
| Editor | `#FFFCF5` | `#2B3238` |
| Text | `#48515A` | `#E2E5DE` |
| Sidebar | `#EEF1E8` | `#262D28` |
| Title bar | `#E9EDF1` | `#22282D` |
| Status bar | `#DCE5D1` | `#354331` |

Brand palette: `#B8C3D3`, `#CEDABF`, `#E1C1D0`, `#EFD1CD`, `#FDECCE`.

## Installation

Use **Extensions: Install from VSIX**, then choose either appearance with **Preferences: Color Theme**.

Includes semantic highlighting, terminal colors, Git decorations, search and selection colors. Full UI colors are listed in `COLOR-SPEC.md`; real VS Code previews are included in `store-assets/screenshots/en/`.

Publisher: **lilinhuang** · Version: **1.0.0**

[Marketplace](https://marketplace.visualstudio.com/items?itemName=lilinhuang.harvest-tapestry-theme)
''',encoding='utf-8')
print('Created',base)


