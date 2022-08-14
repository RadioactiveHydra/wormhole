import setuptools
# Extremely hacky way to get the version to load...
try:
    from wormhole.version import __version__
except ImportError as e:
    from wormhole.version import __version__

# Setup the markdown
readme_markdown = ""
ignore = False
for l in open("README.md"):
    if l.startswith("[HTMLElementBegin]"):
        ignore = True
        continue
    elif l.startswith("[HTMLElementEnd]"):
        ignore = False
        continue
    else:
        readme_markdown += l if not ignore else ""
        
# Setup the requirements
requirements = []
for l in open("requirements.txt"):
    requirements.append(l.strip())

setuptools.setup(
    name='wormhole-video',
    version=__version__,
    description='Simple and Hackable Realtime Video Streaming Engine',
    author='Edward Li',
    url='https://github.com/RadioactiveHydra/Wormhole/',
    packages=['wormhole', 'wormhole.streamer', 'wormhole.video', 'wormhole.viewer'],
    install_requires=requirements,
    long_description=readme_markdown,   
    long_description_content_type='text/markdown',
    project_urls={
        "Bug Reports": f"https://github.com/RadioactiveHydra/Wormhole/issues",
        "Demo": "https://demo.wormhole.hydranet.dev/",
        "Discord": "https://discord.gg/9QF2bPc",
    }
)