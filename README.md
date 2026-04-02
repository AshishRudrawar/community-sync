# Community Sync

[![CI](https://github.com/AshishRudrawar/community-sync/actions/workflows/python-app.yml/badge.svg)](https://github.com/AshishRudrawar/community-sync/actions/workflows/python-app.yml)
[![Dependabot](https://github.com/AshishRudrawar/community-sync/actions/workflows/dependabot.yml/badge.svg)](https://github.com/AshishRudrawar/community-sync/actions/workflows/dependabot.yml)
[![Release](https://github.com/AshishRudrawar/community-sync/actions/workflows/release.yml/badge.svg)](https://github.com/AshishRudrawar/community-sync/actions/workflows/release.yml)

`community-sync` is a CLI tool for generating weekly health reports for GitHub organizations and repos.

## Setup

```bash
cd community-sync
python -m pip install --upgrade pip
python -m pip install -e '.[test]'
```

or with Makefile:

```bash
make install
```

## Features

- `comsync report --org orgname`: gather open issues, PRs, stale items, and contributor stats across org repos
- `comsync summary --repo owner/repo`: output a quick community progress summary

## Quickstart

```bash
comsync report --org octokit
```

## OSS health checks

- [x] Active CI: `python-app.yml`
- [x] Dependency updates: `dependabot.yml`
- [x] Release tags: `release.yml`
- [ ] Star target: 50+ (set goal)
- [ ] Contributors target: 10+ (set goal)

### Quick metrics snapshot

```bash
python scripts/oss_health.py --repo AshishRudrawar/community-sync
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT