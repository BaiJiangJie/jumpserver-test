name: Auto update docs changelog

on:
  release:
    types: [published]

jobs:
  update_docs_changelog:
    runs-on: ubuntu-latest
    if: startsWith(github.event.release.tag_name, 'v4.')
    steps:
      - name: Update docs changelog
        env:
          GITHUB_TOKEN: ${{ secrets.DOCS_ACCESS_TOKEN }}
          TAG_NAME: "${{ github.event.release.tag_name }}
        run:
          git clone git@github.com:jumpservice/documentation.git
          cd documentation/utils && bash update_changelog.sh
          
