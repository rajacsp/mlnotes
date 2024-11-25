---
title: Simple-Beautifulsoup
date: 2024-11-25
author: Your Name
cell_count: 4
score: 0
---

---
title: "Simple BeautifulSoup"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import requests
from bs4 import BeautifulSoup
```


```python
page = requests.get('https://github.com/getify/BikechainJS')
soup = BeautifulSoup(page.text, 'html.parser')    

print(soup) 
```

    
    <!DOCTYPE html>
    
    <html lang="en">
    <head>
    <meta charset="utf-8"/>
    <link href="https://github.githubassets.com" rel="dns-prefetch"/>
    <link href="https://avatars0.githubusercontent.com" rel="dns-prefetch"/>
    <link href="https://avatars1.githubusercontent.com" rel="dns-prefetch"/>
    <link href="https://avatars2.githubusercontent.com" rel="dns-prefetch"/>
    <link href="https://avatars3.githubusercontent.com" rel="dns-prefetch"/>
    <link href="https://github-cloud.s3.amazonaws.com" rel="dns-prefetch"/>
    <link href="https://user-images.githubusercontent.com/" rel="dns-prefetch"/>
    <link crossorigin="anonymous" href="https://github.githubassets.com/assets/frameworks-d69542a4a3958db914b3bec3f757de26.css" integrity="sha512-OBabailf0Gja8rWVZO1xyYAw//CQdLOJF4riG050gTxsVqVD7az4Sq56hPWfv3AoaxuEhYXgQlGQcNxzZzDyVA==" media="all" rel="stylesheet">
    <link crossorigin="anonymous" href="https://github.githubassets.com/assets/site-e4d561c16b6b9aaadbf00c0559c20085.css" integrity="sha512-9f3NsOQR/iafpq5oTq9iaNzpmB3VaUcvR6AtzwqKitGWmnCnxlp4dfbENMlnj8IgKSCuwyrZTQ6Rok0xkfeiLA==" media="all" rel="stylesheet">
    <link crossorigin="anonymous" href="https://github.githubassets.com/assets/github-038ca28f0d66963cc8fcdd04180ca5e0.css" integrity="sha512-wJhnzAfXEZIRVozNeRj3om7LYMKNuN4/pWiws3GvDrVcYuSnHZVWzVFF0nocd7vibgFePdnbVtr/SgFIOP/FcA==" media="all" rel="stylesheet">
    <meta content="width=device-width" name="viewport"/>
    <title>GitHub - getify/BikechainJS: JavaScript VM engine (powered by V8); server-side environment modules; server-side synchronous web app controllers</title>
    <meta content="JavaScript VM engine (powered by V8); server-side environment modules; server-side synchronous web app controllers - getify/BikechainJS" name="description"/>
    <link href="/opensearch.xml" rel="search" title="GitHub" type="application/opensearchdescription+xml"/>
    <link href="https://github.com/fluidicon.png" rel="fluid-icon" title="GitHub"/>
    <meta content="1401488693436528" property="fb:app_id"/>
    <meta content="https://avatars0.githubusercontent.com/u/150330?s=400&amp;v=4" name="twitter:image:src"><meta content="@github" name="twitter:site"><meta content="summary" name="twitter:card"><meta content="getify/BikechainJS" name="twitter:title"><meta content="JavaScript VM engine (powered by V8); server-side environment modules; server-side synchronous web app controllers - getify/BikechainJS" name="twitter:description"/>
    <meta content="https://avatars0.githubusercontent.com/u/150330?s=400&amp;v=4" property="og:image"/><meta content="GitHub" property="og:site_name"/><meta content="object" property="og:type"/><meta content="getify/BikechainJS" property="og:title"/><meta content="https://github.com/getify/BikechainJS" property="og:url"/><meta content="JavaScript VM engine (powered by V8); server-side environment modules; server-side synchronous web app controllers - getify/BikechainJS" property="og:description"/>
    <link href="https://github.githubassets.com/" rel="assets"/>
    <meta content="1000" name="pjax-timeout"/>
    <meta content="C95E:0EFF:3C20D2:6830D0:5CBCDA1E" data-pjax-transient="" name="request-id"/>
    <meta data-pjax-transient="" name="selected-link" value="repo_source"/>
    <meta content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU" name="google-site-verification"/>
    <meta content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA" name="google-site-verification"/>
    <meta content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc" name="google-site-verification"/>
    <meta content="collector.githubapp.com" name="octolytics-host"><meta content="github" name="octolytics-app-id"><meta content="https://collector.githubapp.com/github-external/browser_event" name="octolytics-event-url"><meta content="C95E:0EFF:3C20D2:6830D0:5CBCDA1E" name="octolytics-dimension-request_id"><meta content="iad" name="octolytics-dimension-region_edge"><meta content="iad" name="octolytics-dimension-region_render">
    <meta content="/&lt;user-name&gt;/&lt;repo-name&gt;" data-pjax-transient="true" name="analytics-location"/>
    <meta content="UA-3769691-2" name="google-analytics"/>
    <meta class="js-ga-set" content="Logged Out" name="dimension1"/>
    <meta content="github.com" name="hostname"/>
    <meta content="" name="user-login"/>
    <meta content="github.com" name="expected-hostname"/>
    <meta content="NDY4OGZlN2IxMTNiY2FjY2JkZWI4YjJkZDJiYjQ3YjBkOGNlZmRhNGVlNzVkYmE3MjhhYzI3N2EzNGE0NzlmOXx7InJlbW90ZV9hZGRyZXNzIjoiNTAuMTAwLjMwLjEzNiIsInJlcXVlc3RfaWQiOiJDOTVFOjBFRkY6M0MyMEQyOjY4MzBEMDo1Q0JDREExRSIsInRpbWVzdGFtcCI6MTU1NTg4MDQ3OCwiaG9zdCI6ImdpdGh1Yi5jb20ifQ==" name="js-proxy-site-detection-payload"/>
    <meta content="UNIVERSE_BANNER,MARKETPLACE_INVOICED_BILLING,MARKETPLACE_SOCIAL_PROOF_CUSTOMERS,MARKETPLACE_TRENDING_SOCIAL_PROOF,MARKETPLACE_RECOMMENDATIONS" name="enabled-features"/>
    <meta content="e8eafa1c4ad732748ef256e00a9005a904b1beaf" name="html-safe-nonce"/>
    <meta content="7d174e573145e30ac002780c2257882e" http-equiv="x-pjax-version"/>
    <link href="https://github.com/getify/BikechainJS/commits/master.atom" rel="alternate" title="Recent Commits to BikechainJS:master" type="application/atom+xml"/>
    <meta content="github.com/getify/BikechainJS git https://github.com/getify/BikechainJS.git" name="go-import"/>
    <meta content="150330" name="octolytics-dimension-user_id"><meta content="getify" name="octolytics-dimension-user_login"><meta content="523714" name="octolytics-dimension-repository_id"><meta content="getify/BikechainJS" name="octolytics-dimension-repository_nwo"><meta content="true" name="octolytics-dimension-repository_public"><meta content="false" name="octolytics-dimension-repository_is_fork"><meta content="523714" name="octolytics-dimension-repository_network_root_id"><meta content="getify/BikechainJS" name="octolytics-dimension-repository_network_root_nwo"><meta content="false" name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown">
    <link data-pjax-transient="" href="https://github.com/getify/BikechainJS" rel="canonical"/>
    <meta content="https://api.github.com/_private/browser/stats" name="browser-stats-url"/>
    <meta content="https://api.github.com/_private/browser/errors" name="browser-errors-url"/>
    <link color="#000000" href="https://github.githubassets.com/pinned-octocat.svg" rel="mask-icon"/>
    <link class="js-site-favicon" href="https://github.githubassets.com/favicon.ico" rel="icon" type="image/x-icon"/>
    <meta content="#1e2327" name="theme-color"/>
    <link crossorigin="use-credentials" href="/manifest.json" rel="manifest"/>
    </meta></meta></meta></meta></meta></meta></meta></meta></meta></meta></meta></meta></meta></meta></meta></meta></meta></meta></meta></link></link></link></head>
    <body class="logged-out env-production">
    <div class="position-relative js-header-wrapper">
    <a class="px-2 py-4 bg-blue text-white show-on-focus js-skip-to-content" href="#start-of-content" tabindex="1">Skip to content</a>
    <div class="pjax-loader-bar" id="js-pjax-loader-bar"><div class="progress"></div></div>
    <header class="Header-old header-logged-out position-relative f4 py-2" role="banner">
    <div class="container-lg d-flex px-3">
    <div class="d-flex flex-justify-between flex-items-center">
    <a aria-label="Homepage" class="mr-4" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark" href="https://github.com/">
    <svg aria-hidden="true" class="octicon octicon-mark-github text-white" height="32" version="1.1" viewbox="0 0 16 16" width="32"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z" fill-rule="evenodd"></path></svg>
    </a>
    </div>
    <div class="HeaderMenu HeaderMenu--logged-out d-flex flex-justify-between flex-items-center flex-auto">
    <div class="d-none">
    <button aria-expanded="false" aria-label="Toggle navigation" class="btn-link js-details-target" type="button">
    <svg aria-hidden="true" class="octicon octicon-x text-gray" height="24" version="1.1" viewbox="0 0 12 16" width="18"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z" fill-rule="evenodd"></path></svg>
    </button>
    </div>
    <nav aria-label="Global" class="mt-0">
    <ul class="d-flex list-style-none">
    <li class="mr-3 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center">
    <details class="HeaderMenu-details details-overlay details-reset width-full">
    <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-inline-block">
                        Why GitHub?
                        <svg class="icon-chevon-down-mktg position-relative" fill="none" viewbox="0 0 14 8" x="0px" xml:space="preserve" y="0px">
    <path d="M1,1l6.2,6L13,1"></path>
    </svg>
    </summary>
    <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 mt-0 p-4 left-n4 position-absolute">
    <a class="py-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Features" href="/features">Features <span class="Bump-link-symbol float-right text-normal text-gray-light">→</span></a>
    <ul class="list-style-none f5 pb-3">
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Code review" href="/features/code-review/">Code review</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Project management" href="/features/project-management/">Project management</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Integrations" href="/features/integrations">Integrations</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Actions" href="/features/actions">Actions</a>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Team management" href="/features#team-management">Team management</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Social coding" href="/features#social-coding">Social coding</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Documentation" href="/features#documentation">Documentation</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Code hosting" href="/features#code-hosting">Code hosting</a></li>
    </li></ul>
    <ul class="list-style-none mb-0 border-lg-top pt-lg-3">
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Customer stories" href="/customer-stories">Customer stories <span class="Bump-link-symbol float-right text-normal text-gray-light">→</span></a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Security" href="/security">Security <span class="Bump-link-symbol float-right text-normal text-gray-light">→</span></a></li>
    </ul>
    </div>
    </details>
    </li>
    <li class="mr-3 mr-lg-3">
    <a class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Enterprise" href="/enterprise">Enterprise</a>
    </li>
    <li class="mr-3 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center">
    <details class="HeaderMenu-details details-overlay details-reset width-full">
    <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-inline-block">
                        Explore
                        <svg class="icon-chevon-down-mktg position-relative" fill="none" viewbox="0 0 14 8" x="0px" xml:space="preserve" y="0px">
    <path d="M1,1l6.2,6L13,1"></path>
    </svg>
    </summary>
    <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 pt-2 pb-0 mt-0 p-4 left-n4 position-absolute">
    <ul class="list-style-none mb-3">
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Explore" href="/explore">Explore GitHub <span class="Bump-link-symbol float-right text-normal text-gray-light">→</span></a></li>
    </ul>
    <h4 class="text-gray-light text-normal text-mono f5 mb-2 border-top pt-3">Learn &amp; contribute</h4>
    <ul class="list-style-none mb-3">
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Topics" href="/topics">Topics</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Collections" href="/collections">Collections</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Trending" href="/trending">Trending</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Learning lab" href="https://lab.github.com/">Learning Lab</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Open source guides" href="https://opensource.guide">Open source guides</a></li>
    </ul>
    <h4 class="text-gray-light text-normal text-mono f5 mb-2 border-top pt-3">Connect with others</h4>
    <ul class="list-style-none mb-0">
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Events" href="https://github.com/events">Events</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Community forum" href="https://github.community">Community forum</a></li>
    <li class="edge-item-fix"><a class="py-2 pb-0 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to GitHub Education" href="https://education.github.com">GitHub Education</a></li>
    </ul>
    </div>
    </details>
    </li>
    <li class="mr-3 mr-lg-3">
    <a class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Marketplace" href="/marketplace">Marketplace</a>
    </li>
    <li class="mr-3 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center">
    <details class="HeaderMenu-details details-overlay details-reset width-full">
    <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-inline-block">
                        Pricing
                        <svg class="icon-chevon-down-mktg position-relative" fill="none" viewbox="0 0 14 8" x="0px" xml:space="preserve" y="0px">
    <path d="M1,1l6.2,6L13,1"></path>
    </svg>
    </summary>
    <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 pt-2 pb-4 mt-0 p-4 left-n4 position-absolute">
    <a class="pb-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Pricing" href="/pricing">Plans <span class="Bump-link-symbol float-right text-normal text-gray-light">→</span></a>
    <ul class="list-style-none mb-3">
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Compare plans" href="/pricing#feature-comparison">Compare plans</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Contact Sales" href="https://enterprise.github.com/contact">Contact Sales</a></li>
    </ul>
    <ul class="list-style-none mb-0 border-top pt-3">
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Nonprofits" href="/nonprofit">Nonprofit <span class="Bump-link-symbol float-right text-normal text-gray-light">→</span></a></li>
    <li class="edge-item-fix"><a class="py-2 pb-0 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Education" href="https://education.github.com">Education <span class="Bump-link-symbol float-right text-normal text-gray-light">→</span></a></li>
    </ul>
    </div>
    </details>
    </li>
    </ul>
    </nav>
    <div class="d-flex flex-items-center px-0 text-center text-left">
    <div class="d-lg-flex">
    <div aria-expanded="false" aria-haspopup="listbox" aria-label="Search or jump to" aria-owns="jump-to-results" class="header-search mr-3 scoped-search site-scoped-search js-site-search position-relative js-jump-to" role="combobox">
    <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></div></div></div></div></div></div></header></div></body></html><form accept-charset="UTF-8" action="/getify/BikechainJS/search" aria-label="Site" class="js-site-search-form" data-scope-id="523714" data-scope-type="Repository" data-scoped-search-url="/getify/BikechainJS/search" data-unscoped-search-url="/search" method="get" role="search"><input name="utf8" type="hidden" value="✓"/>
    <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
    <input aria-autocomplete="list" aria-controls="jump-to-results" aria-label="Search" autocapitalize="off" autocomplete="off" class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable" data-hotkey="s,/" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations#csrf-token=lJ58QKCy3J/C0b5T890dTYPus8BYaHVVfv5hNe5zj6vPnIham9S8WRnV4dH2JhD0ax69CHdQbBSBQ7yVRVcN3Q==" data-scoped-placeholder="Search" data-unscoped-placeholder="Search GitHub" name="q" placeholder="Search" spellcheck="false" type="text" value=""/>
    <input class="js-site-search-type-field" name="type" type="hidden"/>
    <img alt="" class="mr-2 header-search-key-slash" src="https://github.githubassets.com/images/search-key-slash.svg"/>
    <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
    <ul class="d-none js-jump-to-suggestions-template-container">
    <li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
    <a class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="" tabindex="-1">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
    <svg aria-label="Repository" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" height="16" role="img" title="Repository" version="1.1" viewbox="0 0 12 16" width="16"><path d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z" fill-rule="evenodd"></path></svg>
    <svg aria-label="Project" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" height="16" role="img" title="Project" version="1.1" viewbox="0 0 15 16" width="16"><path d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z" fill-rule="evenodd"></path></svg>
    <svg aria-label="Search" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" height="16" role="img" title="Search" version="1.1" viewbox="0 0 16 16" width="16"><path d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z" fill-rule="evenodd"></path></svg>
    </div>
    <img alt="" aria-label="Team" class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" height="28" src="" width="28"/>
    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>
    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
    <span aria-label="in this repository" class="js-jump-to-badge-search-text-default d-none">
            In this repository
          </span>
    <span aria-label="in all of GitHub" class="js-jump-to-badge-search-text-global d-none">
            All GitHub
          </span>
    <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
          Jump to
          <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
    </a>
    </li>
    </ul>
    <ul class="d-none js-jump-to-no-results-template-container">
    <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="text-gray">No suggested jump to results</span>
    </li>
    </ul>
    <ul class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container" id="jump-to-results" role="listbox">
    <li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
    <a class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="" tabindex="-1">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
    <svg aria-label="Repository" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" height="16" role="img" title="Repository" version="1.1" viewbox="0 0 12 16" width="16"><path d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z" fill-rule="evenodd"></path></svg>
    <svg aria-label="Project" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" height="16" role="img" title="Project" version="1.1" viewbox="0 0 15 16" width="16"><path d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z" fill-rule="evenodd"></path></svg>
    <svg aria-label="Search" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" height="16" role="img" title="Search" version="1.1" viewbox="0 0 16 16" width="16"><path d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z" fill-rule="evenodd"></path></svg>
    </div>
    <img alt="" aria-label="Team" class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" height="28" src="" width="28"/>
    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>
    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
    <span aria-label="in this repository" class="js-jump-to-badge-search-text-default d-none">
            In this repository
          </span>
    <span aria-label="in all of GitHub" class="js-jump-to-badge-search-text-global d-none">
            All GitHub
          </span>
    <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
          Jump to
          <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
    </a>
    </li>
    <li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
    <a class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="" tabindex="-1">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
    <svg aria-label="Repository" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" height="16" role="img" title="Repository" version="1.1" viewbox="0 0 12 16" width="16"><path d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z" fill-rule="evenodd"></path></svg>
    <svg aria-label="Project" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" height="16" role="img" title="Project" version="1.1" viewbox="0 0 15 16" width="16"><path d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z" fill-rule="evenodd"></path></svg>
    <svg aria-label="Search" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" height="16" role="img" title="Search" version="1.1" viewbox="0 0 16 16" width="16"><path d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z" fill-rule="evenodd"></path></svg>
    </div>
    <img alt="" aria-label="Team" class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" height="28" src="" width="28"/>
    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>
    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
    <span aria-label="in this repository" class="js-jump-to-badge-search-text-default d-none">
            In this repository
          </span>
    <span aria-label="in all of GitHub" class="js-jump-to-badge-search-text-global d-none">
            All GitHub
          </span>
    <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
          Jump to
          <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
    </a>
    </li>
    </ul>
    </div>
    </label>
    </form> 
    
    
    <a class="HeaderMenu-link no-underline mr-3" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in" data-hydro-click='{"event_type":"authentication.click","payload":{"location_in_page":"site header menu","repository_id":null,"auth_type":"LOG_IN","client_id":null,"originating_request_id":"C95E:0EFF:3C20D2:6830D0:5CBCDA1E","originating_url":"https://github.com/getify/BikechainJS","referrer":null,"user_id":null}}' data-hydro-click-hmac="6eafcbb87aa235f8b6805ea150470af7396c062b3cec00af2c151f0461dd09c2" href="/login?return_to=%2Fgetify%2FBikechainJS">
              Sign in
    </a> <a class="HeaderMenu-link d-inline-block no-underline border border-gray-dark rounded-1 px-2 py-1" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up" data-hydro-click='{"event_type":"authentication.click","payload":{"location_in_page":"site header menu","repository_id":null,"auth_type":"SIGN_UP","client_id":null,"originating_request_id":"C95E:0EFF:3C20D2:6830D0:5CBCDA1E","originating_url":"https://github.com/getify/BikechainJS","referrer":null,"user_id":null}}' data-hydro-click-hmac="94a63a331ab83a323c629a6ab1bb5ccfcdf987e27113d845188b1eb1f1b25cb7" href="/join">
                Sign up
    </a> 
    
    
    
    
    <div class="show-on-focus" id="start-of-content"></div>
    <div id="js-flash-container">
    </div>
    <div class="application-main" data-commit-hovercards-enabled="">
    <div class="" itemscope="" itemtype="http://schema.org/SoftwareSourceCode">
    <main data-pjax-container="" id="js-repo-pjax-container">
    <div class="flash flash-warn flash-full border-0 text-center text-bold py-2">
        This repository has been archived by the owner. It is now read-only.
      </div>
    <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
    <div class="repohead-details-container clearfix container">
    <ul class="pagehead-actions">
    <li>
    <a aria-label="You must be signed in to watch a repository" class="tooltipped tooltipped-s btn btn-sm btn-with-count" data-hydro-click='{"event_type":"authentication.click","payload":{"location_in_page":"notification subscription menu watch","repository_id":null,"auth_type":"LOG_IN","client_id":null,"originating_request_id":"C95E:0EFF:3C20D2:6830D0:5CBCDA1E","originating_url":"https://github.com/getify/BikechainJS","referrer":null,"user_id":null}}' data-hydro-click-hmac="f19ca060ada4742290d9a4f0c53d6189a83ee9e7d7f6fb8f3b4414c09ddd00cb" href="/login?return_to=%2Fgetify%2FBikechainJS" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-eye v-align-text-bottom" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z" fill-rule="evenodd"></path></svg>
        Watch
    </a> <a aria-label="6 users are watching this repository" class="social-count" href="/getify/BikechainJS/watchers">
          6
        </a>
    </li>
    <li>
    <a aria-label="You must be signed in to star a repository" class="btn btn-sm btn-with-count tooltipped tooltipped-s" data-hydro-click='{"event_type":"authentication.click","payload":{"location_in_page":"star button","repository_id":523714,"auth_type":"LOG_IN","client_id":null,"originating_request_id":"C95E:0EFF:3C20D2:6830D0:5CBCDA1E","originating_url":"https://github.com/getify/BikechainJS","referrer":null,"user_id":null}}' data-hydro-click-hmac="3ed3e73b6062a8fcf136f58df3eaea885d9dd98db5b5df63fe0e55b59623f762" href="/login?return_to=%2Fgetify%2FBikechainJS" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-star v-align-text-bottom" height="16" version="1.1" viewbox="0 0 14 16" width="14"><path d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z" fill-rule="evenodd"></path></svg>
          Star
    </a>
    <a aria-label="52 users starred this repository" class="social-count js-social-count" href="/getify/BikechainJS/stargazers">
          52
        </a>
    </li>
    <li>
    <a aria-label="You must be signed in to fork a repository" class="btn btn-sm btn-with-count tooltipped tooltipped-s" data-hydro-click='{"event_type":"authentication.click","payload":{"location_in_page":"repo details fork button","repository_id":523714,"auth_type":"LOG_IN","client_id":null,"originating_request_id":"C95E:0EFF:3C20D2:6830D0:5CBCDA1E","originating_url":"https://github.com/getify/BikechainJS","referrer":null,"user_id":null}}' data-hydro-click-hmac="0d9708f6b7e1ccb1cbea104d2c3596adb6f4c5f5a7a556b39c9e924d1b397a26" href="/login?return_to=%2Fgetify%2FBikechainJS" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-repo-forked v-align-text-bottom" height="16" version="1.1" viewbox="0 0 10 16" width="10"><path d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z" fill-rule="evenodd"></path></svg>
            Fork
    </a>
    <a aria-label="8 users forked this repository" class="social-count" href="/getify/BikechainJS/network/members">
          8
        </a>
    </li>
    </ul>
    <h1 class="public">
    <svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewbox="0 0 12 16" width="12"><path d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z" fill-rule="evenodd"></path></svg>
    <span class="author" itemprop="author"><a class="url fn" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=150330" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/getify" rel="author">getify</a></span><!--
    --><span class="path-divider">/</span><!--
    --><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/getify/BikechainJS">BikechainJS</a></strong>
    </h1>
    </div>
    <nav aria-label="Repository" class="reponav js-repo-nav js-sidenav-container-pjax container" data-pjax="#js-repo-pjax-container" itemscope="" itemtype="http://schema.org/BreadcrumbList">
    <span itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <a aria-current="page" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /getify/BikechainJS" href="/getify/BikechainJS" itemprop="url">
    <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewbox="0 0 14 16" width="14"><path d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z" fill-rule="evenodd"></path></svg>
    <span itemprop="name">Code</span>
    <meta content="1" itemprop="position"/>
    </a> </span>
    <span itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <a class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /getify/BikechainJS/issues" href="/getify/BikechainJS/issues" itemprop="url">
    <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewbox="0 0 14 16" width="14"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z" fill-rule="evenodd"></path></svg>
    <span itemprop="name">Issues</span>
    <span class="Counter">0</span>
    <meta content="2" itemprop="position"/>
    </a> </span>
    <span itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <a class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls checks /getify/BikechainJS/pulls" href="/getify/BikechainJS/pulls" itemprop="url">
    <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewbox="0 0 12 16" width="12"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z" fill-rule="evenodd"></path></svg>
    <span itemprop="name">Pull requests</span>
    <span class="Counter">0</span>
    <meta content="3" itemprop="position"/>
    </a> </span>
    <a class="js-selected-navigation-item reponav-item" data-hotkey="g b" data-selected-links="repo_projects new_repo_project repo_project /getify/BikechainJS/projects" href="/getify/BikechainJS/projects">
    <svg aria-hidden="true" class="octicon octicon-project" height="16" version="1.1" viewbox="0 0 15 16" width="15"><path d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z" fill-rule="evenodd"></path></svg>
          Projects
          <span class="Counter">0</span>
    </a>
    <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse people alerts /getify/BikechainJS/pulse" href="/getify/BikechainJS/pulse">
    <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z" fill-rule="evenodd"></path></svg>
          Insights
    </a>
    </nav>
    </div>
    <div class="container new-discussion-timeline experiment-repo-nav">
    <div class="repository-content">
    <div class="signup-prompt-bg rounded-1">
    <div class="signup-prompt p-4 text-center mb-4 rounded-1">
    <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></div></div></div></div></div></main></div></div><form accept-charset="UTF-8" action="/prompt_dismissals/signup" method="post"><input name="utf8" type="hidden" value="✓"><input name="_method" type="hidden" value="put"><input name="authenticity_token" type="hidden" value="2GcG8wDD27ALfb5TTu4AXK74niE/wyvqF3GU8CUi3Hhv4BjY4OhnUMKrhplvSfBRXhpVknBALi/U1VsUQEoLYQ=="/>
    <button class="position-absolute top-0 right-0 btn-link link-gray" data-ga-click="(Logged out) Sign up prompt, clicked Dismiss, text:dismiss" type="submit">
                  Dismiss
                </button>
    </input></input></form> <h3 class="pt-2">Join GitHub today</h3>
    <p class="col-6 mx-auto">GitHub is home to over 31 million developers working together to host and review code, manage projects, and build software together.</p>
    <a class="btn btn-primary" data-ga-click="(Logged out) Sign up prompt, clicked Sign up, text:sign-up" data-hydro-click='{"event_type":"authentication.click","payload":{"location_in_page":"files signup prompt","repository_id":null,"auth_type":"SIGN_UP","client_id":null,"originating_request_id":"C95E:0EFF:3C20D2:6830D0:5CBCDA1E","originating_url":"https://github.com/getify/BikechainJS","referrer":null,"user_id":null}}' data-hydro-click-hmac="3ffe53778c7ad5fa29919d0fe935db98e337e7b0264efbb1fc7b6cdcbf352cde" href="/join?source=prompt-code">Sign up</a>
    
    
    
    <div class="mb-3"> <div class="f4">
    <span class="text-gray-dark mr-2" itemprop="about">
              JavaScript VM engine (powered by V8); server-side environment modules; server-side synchronous web app controllers
            </span>
    <span itemprop="url"><a href="http://getify.com" rel="nofollow">http://getify.com</a></span>
    </div>
    </div>
    <div class="overall-summary overall-summary-bottomless">
    <div class="stats-switcher-viewport js-stats-switcher-viewport">
    <div class="stats-switcher-wrapper">
    <ul class="numbers-summary">
    <li class="commits">
    <a data-pjax="" href="/getify/BikechainJS/commits/master">
    <svg aria-hidden="true" class="octicon octicon-history" height="16" version="1.1" viewbox="0 0 14 16" width="14"><path d="M8 13H6V6h5v2H8v5zM7 1C4.81 1 2.87 2.02 1.59 3.59L0 2v4h4L2.5 4.5C3.55 3.17 5.17 2.3 7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-.34.03-.67.09-1H.08C.03 7.33 0 7.66 0 8c0 3.86 3.14 7 7 7s7-3.14 7-7-3.14-7-7-7z" fill-rule="evenodd"></path></svg>
    <span class="num text-emphasized">
                    25
                  </span>
                  commits
              </a>
    </li>
    <li>
    <a data-pjax="" href="/getify/BikechainJS/branches">
    <svg aria-hidden="true" class="octicon octicon-git-branch" height="16" version="1.1" viewbox="0 0 10 16" width="10"><path d="M10 5c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v.3c-.02.52-.23.98-.63 1.38-.4.4-.86.61-1.38.63-.83.02-1.48.16-2 .45V4.72a1.993 1.993 0 0 0-1-3.72C.88 1 0 1.89 0 3a2 2 0 0 0 1 1.72v6.56c-.59.35-1 .99-1 1.72 0 1.11.89 2 2 2 1.11 0 2-.89 2-2 0-.53-.2-1-.53-1.36.09-.06.48-.41.59-.47.25-.11.56-.17.94-.17 1.05-.05 1.95-.45 2.75-1.25S8.95 7.77 9 6.73h-.02C9.59 6.37 10 5.73 10 5zM2 1.8c.66 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2C1.35 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2zm0 12.41c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm6-8c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z" fill-rule="evenodd"></path></svg>
    <span class="num text-emphasized">
                  1
                </span>
                branch
              </a>
    </li>
    <li>
    <a href="/getify/BikechainJS/releases">
    <svg aria-hidden="true" class="octicon octicon-tag" height="16" version="1.1" viewbox="0 0 14 16" width="14"><path d="M7.73 1.73C7.26 1.26 6.62 1 5.96 1H3.5C2.13 1 1 2.13 1 3.5v2.47c0 .66.27 1.3.73 1.77l6.06 6.06c.39.39 1.02.39 1.41 0l4.59-4.59a.996.996 0 0 0 0-1.41L7.73 1.73zM2.38 7.09c-.31-.3-.47-.7-.47-1.13V3.5c0-.88.72-1.59 1.59-1.59h2.47c.42 0 .83.16 1.13.47l6.14 6.13-4.73 4.73-6.13-6.15zM3.01 3h2v2H3V3h.01z" fill-rule="evenodd"></path></svg>
    <span class="num text-emphasized">
                  0
                </span>
                releases
              </a>
    </li>
    <li>
    <a href="/getify/BikechainJS/graphs/contributors">
    <svg aria-hidden="true" class="octicon octicon-organization" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M16 12.999c0 .439-.45 1-1 1H7.995c-.539 0-.994-.447-.995-.999H1c-.54 0-1-.561-1-1 0-2.634 3-4 3-4s.229-.409 0-1c-.841-.621-1.058-.59-1-3 .058-2.419 1.367-3 2.5-3s2.442.58 2.5 3c.058 2.41-.159 2.379-1 3-.229.59 0 1 0 1s1.549.711 2.42 2.088C9.196 9.369 10 8.999 10 8.999s.229-.409 0-1c-.841-.62-1.058-.59-1-3 .058-2.419 1.367-3 2.5-3s2.437.581 2.495 3c.059 2.41-.158 2.38-1 3-.229.59 0 1 0 1s3.005 1.366 3.005 4z" fill-rule="evenodd"></path></svg>
    <span class="num text-emphasized">
          1
        </span>
        contributor
    </a>
    </li>
    </ul>
    <div class="repository-lang-stats">
    <ol class="repository-lang-stats-numbers">
    <li>
    <a data-ga-click="Repository, language stats search click, location:repo overview" href="/getify/BikechainJS/search?l=c%2B%2B">
    <span class="color-block language-color" style="background-color:#f34b7d;"></span>
    <span class="lang">C++</span>
    <span class="percent">60.3%</span>
    </a>
    </li>
    <li>
    <a data-ga-click="Repository, language stats search click, location:repo overview" href="/getify/BikechainJS/search?l=javascript">
    <span class="color-block language-color" style="background-color:#f1e05a;"></span>
    <span class="lang">JavaScript</span>
    <span class="percent">35.0%</span>
    </a>
    </li>
    <li>
    <a data-ga-click="Repository, language stats search click, location:repo overview" href="/getify/BikechainJS/search?l=c">
    <span class="color-block language-color" style="background-color:#555555;"></span>
    <span class="lang">C</span>
    <span class="percent">4.7%</span>
    </a>
    </li>
    </ol>
    </div>
    </div>
    </div>
    </div>
    <button class="d-flex p-0 repository-lang-stats-graph js-toggle-lang-stats" data-ga-click="Repository, language bar stats toggle, location:repo overview" title="Click for language details" type="button">
    <span aria-label="C++ 60.3%" class="language-color" itemprop="keywords" style="width:60.3%; background-color:#f34b7d;">C++</span>
    <span aria-label="JavaScript 35.0%" class="language-color" itemprop="keywords" style="width:35.0%; background-color:#f1e05a;">JavaScript</span>
    <span aria-label="C 4.7%" class="language-color" itemprop="keywords" style="width:4.7%; background-color:#555555;">C</span>
    </button>
    <div class="file-navigation in-mid-page d-flex flex-items-start">
    <details class="details-reset details-overlay select-menu branch-select-menu">
    <summary class="btn btn-sm select-menu-button css-truncate" data-hotkey="w" title="Switch branches or tags">
    <i>Branch:</i>
    <span class="css-truncate-target">master</span>
    </summary>
    <details-menu class="select-menu-modal position-absolute" preload="" src="/getify/BikechainJS/ref-list/master?source_action=disambiguate&amp;source_controller=files" style="z-index: 99;">
    <include-fragment class="select-menu-loading-overlay anim-pulse">
    <svg aria-hidden="true" class="octicon octicon-octoface" height="32" version="1.1" viewbox="0 0 16 16" width="32"><path d="M14.7 5.34c.13-.32.55-1.59-.13-3.31 0 0-1.05-.33-3.44 1.3-1-.28-2.07-.32-3.13-.32s-2.13.04-3.13.32c-2.39-1.64-3.44-1.3-3.44-1.3-.68 1.72-.26 2.99-.13 3.31C.49 6.21 0 7.33 0 8.69 0 13.84 3.33 15 7.98 15S16 13.84 16 8.69c0-1.36-.49-2.48-1.3-3.35zM8 14.02c-3.3 0-5.98-.15-5.98-3.35 0-.76.38-1.48 1.02-2.07 1.07-.98 2.9-.46 4.96-.46 2.07 0 3.88-.52 4.96.46.65.59 1.02 1.3 1.02 2.07 0 3.19-2.68 3.35-5.98 3.35zM5.49 9.01c-.66 0-1.2.8-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.54-1.78-1.2-1.78zm5.02 0c-.66 0-1.2.79-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.53-1.78-1.2-1.78z" fill-rule="evenodd"></path></svg>
    </include-fragment>
    </details-menu>
    </details>
    <div class="breadcrumb flex-auto">
    </div>
    <div class="BtnGroup">
    <a class="btn btn-sm empty-icon float-right BtnGroup-item" data-ga-click="Repository, find file, location:repo overview" data-hotkey="t" data-hydro-click='{"event_type":"repository.click","payload":{"target":"FIND_FILE_BUTTON","repository_id":523714,"client_id":null,"originating_request_id":"C95E:0EFF:3C20D2:6830D0:5CBCDA1E","originating_url":"https://github.com/getify/BikechainJS","referrer":null,"user_id":null}}' data-hydro-click-hmac="2219ac632e7c2310e1920036d10d36805d9eed2f229bd7bc19e84354822c190f" data-pjax="true" href="/getify/BikechainJS/find/master">Find File</a>
    </div>
    <details class="get-repo-select-menu js-get-repo-select-menu js-anon-get-repo-select-menu position-relative details-overlay details-reset">
    <summary class="btn btn-sm btn-primary" data-hydro-click='{"event_type":"repository.click","payload":{"repository_id":523714,"target":"CLONE_OR_DOWNLOAD_BUTTON","client_id":null,"originating_request_id":"C95E:0EFF:3C20D2:6830D0:5CBCDA1E","originating_url":"https://github.com/getify/BikechainJS","referrer":null,"user_id":null}}' data-hydro-click-hmac="7f8e5b971f620cd761739672d7aa954d97dfaef60af7a3bdb20aa8f50fa95e40">
        Clone or download
        <span class="dropdown-caret"></span>
    </summary> <div class="position-relative">
    <div class="get-repo-modal dropdown-menu dropdown-menu-sw pb-0 js-toggler-container js-get-repo-modal">
    <div class="get-repo-modal-options">
    <div class="clone-options https-clone-options">
    <h4 class="mb-1">
                  Clone with HTTPS
                  <a class="muted-link" href="https://help.github.com/articles/which-remote-url-should-i-use" target="_blank" title="Which remote URL should I use?">
    <svg aria-hidden="true" class="octicon octicon-question" height="16" version="1.1" viewbox="0 0 14 16" width="14"><path d="M6 10h2v2H6v-2zm4-3.5C10 8.64 8 9 8 9H6c0-.55.45-1 1-1h.5c.28 0 .5-.22.5-.5v-1c0-.28-.22-.5-.5-.5h-1c-.28 0-.5.22-.5.5V7H4c0-1.5 1.5-3 3-3s3 1 3 2.5zM7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7z" fill-rule="evenodd"></path></svg>
    </a>
    </h4>
    <p class="mb-2 get-repo-decription-text">
                  Use Git or checkout with SVN using the web URL.
                </p>
    <div class="input-group">
    <input aria-label="Clone this repository at https://github.com/getify/BikechainJS.git" class="form-control input-monospace input-sm" data-autoselect="" readonly="" type="text" value="https://github.com/getify/BikechainJS.git"/>
    <div class="input-group-button">
    <clipboard-copy aria-label="Copy to clipboard" class="btn btn-sm" data-hydro-click='{"event_type":"clone_or_download.click","payload":{"feature_clicked":"COPY_URL","git_repository_type":"REPOSITORY","repository_id":523714,"client_id":null,"originating_request_id":"C95E:0EFF:3C20D2:6830D0:5CBCDA1E","originating_url":"https://github.com/getify/BikechainJS","referrer":null,"user_id":null}}' data-hydro-click-hmac="4ffe18ef68ba1cf03fb0b1f951c3e7d099c00751a8f1a29eb1c831a9654fd37a" value="https://github.com/getify/BikechainJS.git"><svg aria-hidden="true" class="octicon octicon-clippy" height="16" version="1.1" viewbox="0 0 14 16" width="14"><path d="M2 13h4v1H2v-1zm5-6H2v1h5V7zm2 3V8l-3 3 3 3v-2h5v-2H9zM4.5 9H2v1h2.5V9zM2 12h2.5v-1H2v1zm9 1h1v2c-.02.28-.11.52-.3.7-.19.18-.42.28-.7.3H1c-.55 0-1-.45-1-1V4c0-.55.45-1 1-1h3c0-1.11.89-2 2-2 1.11 0 2 .89 2 2h3c.55 0 1 .45 1 1v5h-1V6H1v9h10v-2zM2 5h8c0-.55-.45-1-1-1H8c-.55 0-1-.45-1-1s-.45-1-1-1-1 .45-1 1-.45 1-1 1H3c-.55 0-1 .45-1 1z" fill-rule="evenodd"></path></svg></clipboard-copy>
    </div>
    </div>
    </div>
    <div class="mt-2">
    <a class="btn btn-outline get-repo-btn js-anon-download-zip-link" data-ga-click="Repository, download zip, location:repo overview" data-hydro-click='{"event_type":"clone_or_download.click","payload":{"feature_clicked":"DOWNLOAD_ZIP","git_repository_type":"REPOSITORY","repository_id":523714,"client_id":null,"originating_request_id":"C95E:0EFF:3C20D2:6830D0:5CBCDA1E","originating_url":"https://github.com/getify/BikechainJS","referrer":null,"user_id":null}}' data-hydro-click-hmac="ce2763119dbc2fedbe6773d9b3a17d11854799bd3b60c86580c0eaca58037d0f" href="/getify/BikechainJS/archive/master.zip" rel="nofollow">Download ZIP</a>
    </div>
    </div>
    <div class="js-modal-downloading" hidden="">
    <div class="py-2 px-3">
    <h4 class="lh-condensed mb-3">Downloading<span class="animated-ellipsis-container"><span class="animated-ellipsis">...</span></span></h4>
    <p class="text-gray">
                  Want to be notified of new releases in
                  <span class="text-bold">getify/BikechainJS</span>?
                </p>
    </div>
    <div class="width-full d-flex">
    <a class="get-repo-btn btn btn-outline" data-hydro-click='{"event_type":"authentication.click","payload":{"location_in_page":"download popover","repository_id":523714,"auth_type":"LOG_IN","client_id":null,"originating_request_id":"C95E:0EFF:3C20D2:6830D0:5CBCDA1E","originating_url":"https://github.com/getify/BikechainJS","referrer":null,"user_id":null}}' data-hydro-click-hmac="d292457fbd701d94f2c466dd02ed3dd57d415dfa47d7a9154279ebbc765e0dfd" href="/login?return_to=https%3A%2F%2Fgithub.com%2Fgetify%2FBikechainJS" rel="nofollow" style="width: 50%">Sign in</a>
    <a class="get-repo-btn btn btn-primary" data-hydro-click='{"event_type":"authentication.click","payload":{"location_in_page":"download popover","repository_id":523714,"auth_type":"SIGN_UP","client_id":null,"originating_request_id":"C95E:0EFF:3C20D2:6830D0:5CBCDA1E","originating_url":"https://github.com/getify/BikechainJS","referrer":null,"user_id":null}}' data-hydro-click-hmac="15840a678dac178e107b22ecc3c0f88346fd72ee986c7c231d035e32d784390c" href="/join?return_to=%2Fgetify%2FBikechainJS" rel="nofollow" style="width: 50%">Sign up</a>
    </div>
    </div>
    <div class="js-modal-download-mac py-2 px-3 d-none">
    <h4 class="lh-condensed mb-3">Launching GitHub Desktop<span class="animated-ellipsis-container"><span class="animated-ellipsis">...</span></span></h4>
    <p class="text-gray">If nothing happens, <a href="https://desktop.github.com/">download GitHub Desktop</a> and try again.</p>
    <p><button class="btn-link js-get-repo-modal-download-back">Go back</button></p>
    </div>
    <div class="js-modal-download-windows py-2 px-3 d-none">
    <h4 class="lh-condensed mb-3">Launching GitHub Desktop<span class="animated-ellipsis-container"><span class="animated-ellipsis">...</span></span></h4>
    <p class="text-gray">If nothing happens, <a href="https://desktop.github.com/">download GitHub Desktop</a> and try again.</p>
    <p><button class="btn-link js-get-repo-modal-download-back">Go back</button></p>
    </div>
    <div class="js-modal-download-xcode py-2 px-3 d-none">
    <h4 class="lh-condensed mb-3">Launching Xcode<span class="animated-ellipsis-container"><span class="animated-ellipsis">...</span></span></h4>
    <p class="text-gray">If nothing happens, <a href="https://developer.apple.com/xcode/">download Xcode</a> and try again.</p>
    <p><button class="btn-link js-get-repo-modal-download-back">Go back</button></p>
    </div>
    <div class="js-modal-download-visual-studio py-2 px-3 d-none">
    <h4 class="lh-condensed mb-3">Launching Visual Studio<span class="animated-ellipsis-container"><span class="animated-ellipsis">...</span></span></h4>
    <p class="text-gray">If nothing happens, <a href="https://visualstudio.github.com/">download the GitHub extension for Visual Studio</a> and try again.</p>
    <p><button class="btn-link js-get-repo-modal-download-back">Go back</button></p>
    </div>
    </div>
    </div>
    </details>
    </div>
    <div class="commit-tease js-details-container Details d-flex rounded-top-1" data-issue-and-pr-hovercards-enabled="">
    <div class="AvatarStack flex-self-start">
    <div aria-label="getify" class="AvatarStack-body">
    <a class="avatar" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=150330" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" data-skip-pjax="true" href="/getify">
    <img alt="@getify" height="20" src="https://avatars0.githubusercontent.com/u/150330?s=60&amp;v=4" width="20">
    </img></a> </div>
    </div>
    <div class="flex-auto f6 mr-3">
    <a aria-label="View all commits by getify" class="commit-author tooltipped tooltipped-s user-mention" href="/getify/BikechainJS/commits?author=getify">getify</a>
    <a class="message text-inherit" data-pjax="true" href="/getify/BikechainJS/commit/b42b1a27762ac7cae2f1440fdda01550799e2a77" title="v0.0.2 -- fixed LOTS of bugs with logging">v0.0.2 -- fixed LOTS of bugs with logging</a>
    </div>
    <div class="no-wrap">
          Latest commit
          <a class="commit-tease-sha" data-pjax="" href="/getify/BikechainJS/commit/b42b1a27762ac7cae2f1440fdda01550799e2a77">
            b42b1a2
          </a>
    <span itemprop="dateModified"><relative-time datetime="2011-02-04T00:06:07Z">Feb 4, 2011</relative-time></span>
    </div>
    </div>
    <div class="file-wrap">
    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/getify/BikechainJS/tree/b42b1a27762ac7cae2f1440fdda01550799e2a77">Permalink</a>
    <table class="files js-navigation-container js-active-navigation-container" data-pjax="">
    <thead>
    <tr>
    <th><span class="sr-only">Type</span></th>
    <th><span class="sr-only">Name</span></th>
    <th><span class="sr-only">Latest commit message</span></th>
    <th><span class="sr-only">Commit time</span></th>
    </tr>
    </thead>
    <tbody>
    <tr class="warning include-fragment-error">
    <td class="icon"><svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z" fill-rule="evenodd"></path></svg></td>
    <td class="content" colspan="3">Failed to load latest commit information.</td>
    </tr>
    <tr class="js-navigation-item">
    <td class="icon">
    <svg aria-label="directory" class="octicon octicon-file-directory" height="16" role="img" version="1.1" viewbox="0 0 14 16" width="14"><path d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z" fill-rule="evenodd"></path></svg>
    <img alt="" class="spinner" height="16" src="https://github.githubassets.com/images/spinners/octocat-spinner-32.gif" width="16">
    </img></td>
    <td class="content">
    <span class="css-truncate css-truncate-target"><a class="js-navigation-open" href="/getify/BikechainJS/tree/master/engine" id="ad1943a9fd6d3d7ee1e6af41a5b0d3e7-c534aff85e0b7f65f6481f8a3e523a65c0413865" title="engine">engine</a></span>
    </td>
    <td class="message">
    <span class="css-truncate css-truncate-target">
    <a class="link-gray" data-pjax="true" href="/getify/BikechainJS/commit/b42b1a27762ac7cae2f1440fdda01550799e2a77" title="v0.0.2 -- fixed LOTS of bugs with logging">v0.0.2 -- fixed LOTS of bugs with logging</a>
    </span>
    </td>
    <td class="age">
    <span class="css-truncate css-truncate-target"><time-ago datetime="2011-02-04T00:06:07Z">Feb 4, 2011</time-ago></span>
    </td>
    </tr>
    <tr class="js-navigation-item">
    <td class="icon">
    <svg aria-label="directory" class="octicon octicon-file-directory" height="16" role="img" version="1.1" viewbox="0 0 14 16" width="14"><path d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z" fill-rule="evenodd"></path></svg>
    <img alt="" class="spinner" height="16" src="https://github.githubassets.com/images/spinners/octocat-spinner-32.gif" width="16">
    </img></td>
    <td class="content">
    <span class="css-truncate css-truncate-target"><a class="js-navigation-open" href="/getify/BikechainJS/tree/master/logs" id="2165e4fa5bddb65a31f6a0c495c2fa37-197a56220cad1446ccbbb5c62e61d9ae7f6414f2" title="logs">logs</a></span>
    </td>
    <td class="message">
    <span class="css-truncate css-truncate-target">
    <a class="link-gray" data-pjax="true" href="/getify/BikechainJS/commit/b54fc6f18ff2c5d60d298bbb42f63dfab661e50f" title="ignoring .gitignore itself, and any/all log files">ignoring .gitignore itself, and any/all log files</a>
    </span>
    </td>
    <td class="age">
    <span class="css-truncate css-truncate-target"><time-ago datetime="2011-01-20T16:50:37Z">Jan 20, 2011</time-ago></span>
    </td>
    </tr>
    <tr class="js-navigation-item">
    <td class="icon">
    <svg aria-label="directory" class="octicon octicon-file-directory" height="16" role="img" version="1.1" viewbox="0 0 14 16" width="14"><path d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z" fill-rule="evenodd"></path></svg>
    <img alt="" class="spinner" height="16" src="https://github.githubassets.com/images/spinners/octocat-spinner-32.gif" width="16">
    </img></td>
    <td class="content">
    <span class="css-truncate css-truncate-target"><a class="js-navigation-open" href="/getify/BikechainJS/tree/master/misc" id="bc957e26ff41470c556ee5d09e96880b-a4d526365eea2dc14be042cd3571713eecddc393" title="misc">misc</a></span>
    </td>
    <td class="message">
    <span class="css-truncate css-truncate-target">
    <a class="link-gray" data-pjax="true" href="/getify/BikechainJS/commit/fe439582591e19365d7b949a8e8894aecea84a3c" title="v0.0.1.9 -- added config file parsing and basic logging facility, as well as corrected significant issues with working directory path detection">v0.0.1.9 -- added config file parsing and basic logging facility, as …</a>
    </span>
    </td>
    <td class="age">
    <span class="css-truncate css-truncate-target"><time-ago datetime="2011-01-20T00:30:39Z">Jan 20, 2011</time-ago></span>
    </td>
    </tr>
    <tr class="js-navigation-item">
    <td class="icon">
    <svg aria-label="directory" class="octicon octicon-file-directory" height="16" role="img" version="1.1" viewbox="0 0 14 16" width="14"><path d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z" fill-rule="evenodd"></path></svg>
    <img alt="" class="spinner" height="16" src="https://github.githubassets.com/images/spinners/octocat-spinner-32.gif" width="16"/>
    </td>
    <td class="content">
    <span class="css-truncate css-truncate-target"><a class="js-navigation-open" href="/getify/BikechainJS/tree/master/modules" id="0eb9b3af2e4a00837a1b1a854c9ea18c-465bd9209e5bc3edb11c6c21194acbc4f007e01b" title="modules">modules</a></span>
    </td>
    <td class="message">
    <span class="css-truncate css-truncate-target">
    <a class="link-gray" data-pjax="true" href="/getify/BikechainJS/commit/b42b1a27762ac7cae2f1440fdda01550799e2a77" title="v0.0.2 -- fixed LOTS of bugs with logging">v0.0.2 -- fixed LOTS of bugs with logging</a>
    </span>
    </td>
    <td class="age">
    <span class="css-truncate css-truncate-target"><time-ago datetime="2011-02-04T00:06:07Z">Feb 4, 2011</time-ago></span>
    </td>
    </tr>
    <tr class="js-navigation-item">
    <td class="icon">
    <svg aria-label="file" class="octicon octicon-file" height="16" role="img" version="1.1" viewbox="0 0 12 16" width="12"><path d="M6 5H2V4h4v1zM2 8h7V7H2v1zm0 2h7V9H2v1zm0 2h7v-1H2v1zm10-7.5V14c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V2c0-.55.45-1 1-1h7.5L12 4.5zM11 5L8 2H1v12h10V5z" fill-rule="evenodd"></path></svg>
    <img alt="" class="spinner" height="16" src="https://github.githubassets.com/images/spinners/octocat-spinner-32.gif" width="16"/>
    </td>
    <td class="content">
    <span class="css-truncate css-truncate-target"><a class="js-navigation-open" href="/getify/BikechainJS/blob/master/.gitignore" id="a084b794bc0759e7a6b77810e01874f2-ccd768446a5c63a8f12de29036c7b70aa16b0de8" title=".gitignore">.gitignore</a></span>
    </td>
    <td class="message">
    <span class="css-truncate css-truncate-target">
    <a class="link-gray" data-pjax="true" href="/getify/BikechainJS/commit/dd3e58aa3b33a08bfbfcc46f8daea30a8433e5e1" title="ignore engine binary and makefile">ignore engine binary and makefile</a>
    </span>
    </td>
    <td class="age">
    <span class="css-truncate css-truncate-target"><time-ago datetime="2011-01-20T18:38:50Z">Jan 20, 2011</time-ago></span>
    </td>
    </tr>
    <tr class="js-navigation-item">
    <td class="icon">
    <svg aria-label="file" class="octicon octicon-file" height="16" role="img" version="1.1" viewbox="0 0 12 16" width="12"><path d="M6 5H2V4h4v1zM2 8h7V7H2v1zm0 2h7V9H2v1zm0 2h7v-1H2v1zm10-7.5V14c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V2c0-.55.45-1 1-1h7.5L12 4.5zM11 5L8 2H1v12h10V5z" fill-rule="evenodd"></path></svg>
    <img alt="" class="spinner" height="16" src="https://github.githubassets.com/images/spinners/octocat-spinner-32.gif" width="16"/>
    </td>
    <td class="content">
    <span class="css-truncate css-truncate-target"><a class="js-navigation-open" href="/getify/BikechainJS/blob/master/README.txt" id="26fd799ea07494916e9da9b91b2aac64-77ef6717ddc7159c63cc6327a03bd4e63415ca59" title="README.txt">README.txt</a></span>
    </td>
    <td class="message">
    <span class="css-truncate css-truncate-target">
    <a class="link-gray" data-pjax="true" href="/getify/BikechainJS/commit/fe439582591e19365d7b949a8e8894aecea84a3c" title="v0.0.1.9 -- added config file parsing and basic logging facility, as well as corrected significant issues with working directory path detection">v0.0.1.9 -- added config file parsing and basic logging facility, as …</a>
    </span>
    </td>
    <td class="age">
    <span class="css-truncate css-truncate-target"><time-ago datetime="2011-01-20T00:30:39Z">Jan 20, 2011</time-ago></span>
    </td>
    </tr>
    </tbody>
    </table>
    </div>
    <div class="Box Box--condensed instapaper_body txt js-code-block-container" id="readme">
    <div class="Box-header d-flex flex-items-center flex-justify-between px-2">
    <h3 class="Box-title pr-3">
    <svg aria-hidden="true" class="octicon octicon-book" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z" fill-rule="evenodd"></path></svg>
            README.txt
          </h3>
    </div>
    <div class="Box-body">
    <div class="plain"><pre style="white-space: pre-wrap">BikechainJS Engine
    v0.0.1.9 (c) 2010 Kyle Simpson
    MIT License
    
    
    BikechainJS is a minimal server-side JavaScript wrapper environment (engine) around V8. It consists of a single executable "engine" which takes one or more JavaScript files as arguments, and executes them.
    
    "engine.js" is the bootstrapper for the global environment setup. It is required (in the same directory as the "engine") and is automatically loaded, so must not be manually specified to be loaded.
    
    
    --------------
    
    Installation:
    
    1. Make sure you have a compiled, functional V8:  <a href="http://code.google.com/p/v8/" rel="nofollow">http://code.google.com/p/v8/</a>
     -- NOTE: You need to use V8 v2.1.2+ because a bug was fixed with revision 3924
    
    2. If you created the "shared" V8 library (recommended), proceed to step 4.
    
    3. If you created the "static" V8 library, edit the makefile to reference to proper static library file.
    
    4. Run "make install" and then "make clean".
    
    5. You should now have a "engine" executable in the [root]/engine/ directory. You can execute a JavaScript file by passing it as a parameter to engine, like this:
    
    ./engine dosomething.js
    
    6. You can configure your BikechainJS instance by editing values in the engine.json file, also in the [root]/engine/ directory.
    
    7. Make sure the [root]/logs directory is writeable by the user/process executing bikechain.
    
    
    --------------
    
    Provided global environment:
    
    1. require(module-name): require() is used to load a module. The module name is case-sensitive and must not contain the file extension (.js). A loaded module does not automatically create anything in the global namespace. Instead, the module instance is instead returned from the require() call.
    
    2. include(path-to-file,[forceReload]): include() is used to load/parse a javascript file into the executing environment. The filename should be specified completely, including any relative or absolute path as necessary. "forceReload" is an optional bool parameter (defaults to false) forces the module sub-system to reload the module manually from the file system. Otherwise, modules are cached when loaded to improve performance.
    
    3. include_once(path-to-file): will ensure an exact file (via path) only gets loaded/parsed once.
    
    4. alert() maps to [system].stdout.print(). console.info(), console.log(), console.warn(), and console.error() all send messages to the logs.
    
    5. exit() to immediately stop execution of any javascript in this instance and flush output.
    
    
    --------------
    
    Modules (provided in [root]/modules/):
    
    Several modules are available to be loaded into the executing environment by using the global require() function.
    
    1. "system": System (standard I/O)
    
     *  [system].stdout.write(str): writes "str" to the standard output
     *  [system].stdout.print(str): writes "str" to the standard output, followed by a new-line
     *  [system].stdout.flush(): flushes the output buffer (if necessary)
     *  [system].stdin.read(nonblocking[=true]): if non-blocking (default), if stdin has any buffered, reads from stdin up until an EOF. Otherwise, read returns empty immediately. If not non-blocking, read() blocks waiting for input.
     *  [system].stderr.write(str): same as stdout.write()
     *  [system].stderr.print(str): same as stdout.print()
     *  [system].stderr.flush(): same as stdout.flush()
    
    
    2. "fs": Filesystem (file I/O)
    
     *  [fs].read(file): returns the entire contents of the file
     *  [fs].write(file,str): writes "str" to "file"
    
    
    3. "os": Operating System (process execution)
    
     *  [os].execute(input, cmd, [..cmds, ..]): execute a command on the local system, specified by "cmd" and "cmds" parameters
        -- returns iopipe:
             [iopipe].stdout.read(): reads the output from the executed command
    
    
    4. "promise": "Promises" (sync/async deferral)
    
     * [promise](func): Example: var Promise = require("promise"); Promise(func);
       --Passes a promise "P" object to func as first parameter
         -- "P" has a .fulfill([val]) function which specifies the promise is finished/fulfilled, and optionally passes along a "val" value.
       --Returns an object that can be chained off of, with a .then(func) function, which gets a promise object "P" passed to it
         -- "P" has a .value property which is the chained/passed value from the fulfilled promise
    
     Example:
    
     var Promise = require("promise");
     Promise(function(P){
     	doAsync(function(){ P.fullfill("Done"); });
     })
     .then(function(P){
     	alert(P.value); // "Done"
     });
    
    
    5. "sbfunction": "Sandbox Functions" (protects special core functions by sandboxing them)
    
     * [sb](func): Example: var sbfunc = require("sbfunction"); func = sbfunc(func);
       --sandboxes the passed in function and returns it
    
     Example:
    
     function myfunc() { ... }
    
     var sbfunc = require("sbfunction");
     var myfunc = sbfunc(myfunc);
    
    6. "request": Request Handler (utilities for managing the inbound REQUEST)
    
     * [request].parse(REQUEST): parses the request for GET, POST, COOKIE, and other helpful environment variables
       --Returns the augmented REQUEST object
     * [request].value(REQUEST, name): retrieves the value (if any) of the variable `name` from GET or POST
       --Returns the string value of variable `name`
     * [request].exists(REQUEST, name): determines if the variable `name` exists in GET or POST
       --Returns true/false boolean
    
    7. "response": Response Handler (utilities for managing the outbound RESPONSE)
    
     * [response].Header(name, value): sends a response header
     * [response].Output(name, value): ends response headers' section and begin content body
     * [response].SetCookie(name, value, domain, path, expires): sends a Set-Cookie header
     * [response].SessionCookie(session_name, session_id, domain, path, expires): sends a session cookie header
    
    8. "router": URI Router (handles routing decisions)
    
     * [router].RegisterRouters(routes_filename): reads and registers route rules from `routes_filename`
       --Returns true/false boolean
     * [router].HandleRequest(REQUEST): determines if the REQUEST should be handled, based on the route rules
       --Returns true/false boolean
     * [router].RequestPath(): retrieves the RELATIVE_REQUEST_PATH from the REQUEST
       --Returns the string value of the RELATIVE_REQUEST_PATH of the REQUEST
    
    9. "storage": Storage (stateful "LocalStorage/SessionStorage" functionality in server-side middle-end)
    
     * [storage].Init(sessionID=null): initializes the storage engine, either to an existing session (if sessionID
                                       is passed) or starting a new session.
       --Returns sessionID of session initialized
    
    NOTE: this module is still newly under development.
    
      </pre></div>
    </div>
    </div>
    
    <div class="modal-backdrop js-touch-events"></div>
    
    
    
    
    <div class="footer container-lg width-full px-3" role="contentinfo">
    <div class="position-relative d-flex flex-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light">
    <ul class="list-style-none d-flex flex-wrap">
    <li class="mr-3">© 2019 <span title="0.21881s from unicorn-5494d8bf94-brf5b">GitHub</span>, Inc.</li>
    <li class="mr-3"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
    <li class="mr-3"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
    <li class="mr-3"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
    <li class="mr-3"><a data-ga-click="Footer, go to status, text:status" href="https://githubstatus.com/">Status</a></li>
    <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>
    <a aria-label="Homepage" class="footer-octicon mx-lg-4" href="https://github.com" title="GitHub">
    <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewbox="0 0 16 16" width="24"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z" fill-rule="evenodd"></path></svg>
    </a>
    <ul class="list-style-none d-flex flex-wrap">
    <li class="mr-3"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
    <li class="mr-3"><a data-ga-click="Footer, go to Pricing, text:Pricing" href="https://github.com/pricing">Pricing</a></li>
    <li class="mr-3"><a data-ga-click="Footer, go to api, text:api" href="https://developer.github.com">API</a></li>
    <li class="mr-3"><a data-ga-click="Footer, go to training, text:training" href="https://training.github.com">Training</a></li>
    <li class="mr-3"><a data-ga-click="Footer, go to blog, text:blog" href="https://github.blog">Blog</a></li>
    <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>
    </ul>
    </div>
    <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
    </div>
    </div>
    <div class="ajax-error-message flash flash-error" id="ajax-error-message">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z" fill-rule="evenodd"></path></svg>
    <button aria-label="Dismiss error" class="flash-close js-ajax-error-dismiss" type="button">
    <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewbox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z" fill-rule="evenodd"></path></svg>
    </button>
        You can’t perform that action at this time.
      </div>
    <script crossorigin="anonymous" integrity="sha512-5g98V2j8YTLsw7llCJHOsXoeKDJzBaS1EPqZe/YOBBiPXDE/+5S1WkRoX6AVs/hXTzyJGB3x95OKNDat4vpk0A==" src="https://github.githubassets.com/assets/compat-bootstrap-3ee7f90c.js" type="application/javascript"></script>
    <script crossorigin="anonymous" integrity="sha512-4ogGmCoGByNTJS1EuaHWf5OW9jaaUimTV7C1yWJY2cewmcDQ2BxWQA6/AULidNxvYt3uagTFcU1CQsobKN01XQ==" src="https://github.githubassets.com/assets/frameworks-1f9870ed.js" type="application/javascript"></script>
    <script async="async" crossorigin="anonymous" integrity="sha512-ndUkGfxixq38E/uBsdXO4speen983F90aEEOnJrL67GsP+YOemia80Qo3NInrqoYqn5dDv5QpLvXcYlvUsyyTQ==" src="https://github.githubassets.com/assets/github-bootstrap-afe22710.js" type="application/javascript"></script>
    <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner" hidden="">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z" fill-rule="evenodd"></path></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
    </div>
    <template id="site-details-dialog">
    <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark" open="">
    <summary aria-haspopup="dialog" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast">
    <button aria-label="Close dialog" class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" data-close-dialog="" type="button">
    <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewbox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z" fill-rule="evenodd"></path></svg>
    </button>
    <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
    </details>
    </template>
    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
    <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
    </div>
    </div>
    <div aria-live="polite" class="js-global-screen-reader-notice sr-only"></div>
    
    
    



```python

```


---
**Score: 0**