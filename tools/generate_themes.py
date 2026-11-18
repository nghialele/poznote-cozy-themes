from pathlib import Path

root = Path(__file__).resolve().parents[1]
light = {
"hearth": ("#f5efe4","#eee5d6","#e9decc","#e2d5c1","#e8ddcb","#f0e7d9","#ece2d2","#e6d5bd","#f5efe4","#34271f","#43352b","#5f4d3f","#786555","#8d7a68","#e7dccb","#d8c8b1","#c9b596","#a85f3d","#85472d","#78432f","#ead6c6","168, 95, 61","#914b30","#713a27","145, 75, 48","#85472d"),
"greenhouse": ("#f4f2e9","#e9ecdf","#e2e7d8","#dce2d1","#e7ebdd","#eef0e5","#e8ecdf","#dce6d6","#f4f2e9","#26342b","#35443a","#4e5e51","#657465","#829080","#e0e5d8","#d0d8c8","#bdcbb5","#5f795d","#496449","#3f5b45","#dce7d8","95, 121, 93","#4a684d","#36543b","74, 104, 77","#45664a"),
"rainy-window": ("#eff2f2","#e4ebed","#dce5e8","#d2dde0","#e1e9eb","#edf1f1","#e2eaec","#dbe6e8","#eff2f2","#26383e","#354a51","#4d646b","#637980","#82959a","#dbe4e6","#c8d5d9","#b6c7cc","#a56e52","#82523c","#704632","#eadbd1","165, 110, 82","#804e38","#663c2b","128, 78, 56","#804e38"),
"library-moss": ("#f1f0e5","#e7e8d9","#dfe2d0","#d4d9c1","#e3e5d6","#ececdf","#e3e5d6","#dce3d2","#f1f0e5","#2c3528","#3c4736","#56614d","#6d7764","#899080","#dfe3d5","#ced5c4","#b9c4ac","#68764e","#515e3c","#424e32","#dfe6d2","104, 118, 78","#4e603b","#3b4a2c","78, 96, 59","#4e603b"),
"sunday-linen": ("#f6f2e9","#eee9df","#e9e2d6","#dfd6c8","#ece6db","#f2ede4","#ebe4d8","#eee1ce","#f6f2e9","#38322c","#484139","#625950","#7a7065","#92877b","#e8dfd2","#d9cebf","#c9baa7","#ad7861","#8e5e4a","#754b3c","#efdfd4","173, 120, 97","#865740","#684231","134, 87, 64","#865740"),
"cocoa-nook": ("#f2e9dc","#e8ddce","#dfd1bf","#d5c4af","#e4d7c5","#eee3d4","#e6d8c5","#e8d2bb","#f2e9dc","#392c25","#4b3a30","#665247","#806c60","#968174","#e2d5c4","#d2c1ad","#c0ab94","#a66a43","#825134","#6b422c","#ead6c3","166, 106, 67","#7e4d32","#613b27","126, 77, 50","#7e4d32"),
"fireside-cardigan": ("#f3ece5","#e9ddd5","#e3d3ca","#d8c6bc","#e7d9d0","#efe5dd","#e8d9cf","#ead4c9","#f3ece5","#3a2d2a","#4b3a36","#66524d","#7e6862","#97817a","#e8ddd7","#d7c7bf","#c5b1a7","#a75e53","#84463f","#6d3934","#ead6d0","167, 94, 83","#843f38","#69312d","132, 63, 56","#843f38"),
"bookshop-cat": ("#f3eddf","#e9e0ce","#e2d7c2","#d8c9b0","#e6dcc9","#efe7d7","#e8deca","#e9d9b5","#f3eddf","#342d24","#463c30","#5e5142","#776858","#928170","#e4dac8","#d2c2aa","#bfac8d","#80664c","#664e38","#503d2d","#e7dfce","128, 102, 76","#654a34","#4e3828","101, 74, 52","#654a34"),
"toasted-chai": ("#f4ecdf","#eadfce","#e3d5c0","#d9c8af","#e7dbc6","#f0e5d4","#e9dbc4","#ead6b8","#f4ecdf","#382f24","#4b3e2d","#665744","#806d58","#96836c","#e5dac8","#d4c2a9","#c2ac8f","#a1793f","#805d2d","#674923","#e8dbbe","161, 121, 63","#78572d","#5e4321","120, 87, 45","#78572d"),
"fern-fig": ("#f0eee5","#e5e6da","#dce0d0","#d1d7c2","#e0e3d5","#eaecdf","#e2e5d5","#dce4d2","#f0eee5","#29342b","#3a473b","#526151","#697969","#829183","#dde3d7","#cbd5c8","#b7c5b3","#795b68","#604655","#4e3946","#e6dbe3","121, 91, 104","#654858","#4e3646","101, 72, 88","#654858"),
"peach-scone": ("#f7eee7","#efe1d7","#e9d7ca","#dec9ba","#edddd2","#f3e8df","#ecddd2","#f0d8c9","#f7eee7","#3d2d28","#503c35","#6b534b","#856b62","#9b8177","#eaded6","#d8c7bc","#c6b0a2","#b2674e","#8f4e3a","#743e2f","#f1d9cb","178, 103, 78","#8c4a37","#6f392c","140, 74, 55","#8c4a37"),
"apricot-jam": ("#f7efe2","#efe3d1","#ead9c2","#dfcbae","#ecdfcc","#f3e9d9","#eddfc9","#f0d7b8","#f7efe2","#3b2d22","#4e3d2e","#69533f","#826d57","#9a826a","#eadfce","#d9c8b2","#c8b294","#bf7140","#994f2d","#7a3d23","#f3dcc5","191, 113, 64","#934a2b","#743a22","147, 74, 43","#934a2b"),
"cabin-quilt": ("#f1eee5","#e6e2d7","#ddd8ca","#d2cbb9","#e1ddd1","#ece8dd","#e3ded1","#e4dbc9","#f1eee5","#30322c","#41443b","#5b5e53","#74776a","#8c8f82","#dfdbd0","#cdc7ba","#bab1a0","#8c6855","#704e3e","#593d31","#e7dcd2","140, 104, 85","#704b39","#563929","112, 75, 57","#704b39"),
}
# tuple order follows shared key list
keys=['bg','surface','surface-hover','surface-sunken','chrome-bg','sidebar-surface','code-bg','active-bg','tab-active-bg','text-strong','text','text-secondary','text-muted','text-subtle','border-light','border','border-strong','accent','accent-hover','accent-strong','accent-soft','accent-rgb','accent-text','accent-text-hover','accent-text-rgb','link']

def css(name, vals, dark=False):
    selector="html[data-theme='dark']" if dark else ':root'
    names={'bg':'bg','surface':'surface','surface-hover':'surface-hover','surface-sunken':'surface-sunken','surface-strong':'surface-strong','surface-strong-hover':'surface-strong-hover','chrome-bg':'chrome-bg','sidebar-bg':'sidebar-bg','sidebar-surface':'sidebar-surface','code-bg':'code-bg','active-bg':'active-bg','tabbar-bg':'tabbar-bg','tab-bg':'tab-bg','tab-hover-bg':'tab-hover-bg','tab-active-bg':'tab-active-bg','text-strong':'text-strong','text':'text','text-secondary':'text-secondary','text-muted':'text-muted','text-subtle':'text-subtle','text-inverse':'text-inverse','border-light':'border-light','border':'border','border-strong':'border-strong','accent':'accent','accent-hover':'accent-hover','accent-strong':'accent-strong','accent-soft':'accent-soft','accent-rgb':'accent-rgb','accent-text':'accent-text','accent-text-hover':'accent-text-hover','accent-text-rgb':'accent-text-rgb','link':'link','selection':'selection'}
    d=dict(zip(keys,vals)); d.update({'surface-strong': vals[3], 'surface-strong-hover': vals[2], 'sidebar-bg': vals[4], 'tabbar-bg': vals[4], 'tab-bg': vals[5], 'tab-hover-bg': vals[2], 'text-inverse': vals[0], 'selection':f'rgba({vals[21]}, 0.22)'})
    return f"/* {name} — {'dark reading-room palette' if dark else 'cozy light palette'}. */\n{selector} {{\n"+''.join(f'  --pz-{names[k]}: {v};\n' for k,v in d.items())+'}\n'

for name, vals in light.items():
    # keep existing two themes in place; generate the rest into organized collection.
    if name in ('hearth','greenhouse'): continue
    p=root/'themes'/'light'/f'{name}.css'; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(css(name.replace('-',' ').title(), vals))

dark={
"midnight-library":("#171b1c","#202627","#293132","#111516","#1c2223","#252c2d","#111718","#2d3535","#1c2223","#f0eadc","#e3dccd","#c7c0b2","#aaa597","#878478","#303738","#3a4242","#4a5352","#b98a61","#d0a77c","#d8b58d","#44382c","185, 138, 97","#d0a77c","#e0bd94","208, 167, 124","#d0a77c"),
"emberlight":("#201a18","#29211e","#342925","#171211","#251d1a","#302622","#171311","#3b2a25","#251d1a","#f3e6d8","#e8d9ca","#cdb7a5","#b49b88","#907968","#392e29","#493a33","#5b483e","#c9784e","#e09063","#e6a27a","#4a3027","201, 120, 78","#e09063","#f0a77c","224, 144, 99","#e09063"),
"rain-roof":("#171c22","#202831","#293541","#11161c","#1b232b","#252f39","#11171d","#2d3b45","#1b232b","#e6edf0","#d8e3e8","#b8c8d0","#99adb8","#778c97","#303b44","#3d4b56","#4b5d68","#d08c62","#e0a37c","#e7b491","#3a302d","208, 140, 98","#e0a37c","#efb38e","224, 163, 124","#e0a37c"),
"moss-at-dusk":("#1b201b","#242b23","#2e382c","#141914","#20271f","#2a3228","#151a14","#344030","#20271f","#e8eadf","#dce1d2","#bdc9b5","#9eae96","#7e9078","#333d31","#404d3c","#50614b","#91aa78","#aac38e","#bdd2a5","#303b2c","145, 170, 120","#aac38e","#bed4a3","170, 195, 142","#aac38e"),
"cocoa-after-hours":("#211c19","#2a231f","#352c26","#171311","#251f1b","#302823","#171310","#3b3028","#251f1b","#f0e5d8","#e4d7c9","#cbb8a6","#ad9986","#8c7866","#3a302a","#493c33","#5a493d","#c18b55","#d6a36d","#e0b987","#41332a","193, 139, 85","#d6a36d","#e6b77e","214, 163, 109","#d6a36d"),
"candlelit-desk":("#1d1d20","#272629","#323034","#151518","#222125","#2c2b2e","#151518","#373237","#222125","#f0e9e0","#e5ddd2","#c9bfb4","#aaa096","#887f76","#353337","#444146","#555158","#c29a63","#d8b276","#e4c18e","#3b3329","194, 154, 99","#d8b276","#e8c18c","216, 178, 118","#d8b276"),
"blue-hour-blanket":("#18202a","#202a36","#2a3745","#111720","#1b2530","#252f3c","#121923","#2d3c4c","#1b2530","#edf0f3","#dfe5eb","#bec9d5","#9eacbb","#7f8e9d","#313c49","#3d4a59","#4c5b6c","#9bb4c7","#b1cadb","#c5dae7","#2d3b48","155, 180, 199","#b1cadb","#c4dceb","177, 202, 219","#b1cadb"),
"pine-cabin":("#171f1b","#202a24","#2b372f","#111713","#1b251f","#252f29","#121812","#304036","#1b251f","#e8eee8","#dbe6dc","#b9cbbb","#98ae9a","#788f7b","#303d34","#3d4c42","#4c5f51","#8eb69a","#a6c8ad","#bed9c2","#2e3d33","142, 182, 154","#a6c8ad","#bfddc7","166, 200, 173","#a6c8ad"),
}
for name, vals in dark.items():
    p=root/'themes'/'dark'/f'{name}.css'; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(css(name.replace('-',' ').title(),vals,True))
