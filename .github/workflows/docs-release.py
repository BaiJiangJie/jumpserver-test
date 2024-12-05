name: Publish Release to Discord

on:
  release:
    types: [published]

jobs:
  send_discord_notification:
    runs-on: ubuntu-latest
    if: startsWith(github.event.release.tag_name, 'v4.')
    steps:
      - name: Trigger code change in `b` repository
        env:
          GITHUB_TOKEN: ${{ secrets.DOCS_ACCESS_TOKEN }}
          TAG_NAME: "${{ github.event.release.tag_name }}
        run:
          git clone git@github.com:jumpservice/documentation.git
          cd documentation/utils && bash update_changelog.sh
          
