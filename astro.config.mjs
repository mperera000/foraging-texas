// @ts-check
import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";

import sitemap from "@astrojs/sitemap";

export default defineConfig({
  // The live URL. Needed for the sitemap and for absolute og:image links so
  // shared pages unfurl correctly. Update if the Cloudflare project name differs.
  site: "https://texas-foraging.pages.dev",

  vite: {
    plugins: [tailwindcss()],
  },

  integrations: [sitemap()],
});