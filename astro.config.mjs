// @ts-check
import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";

import sitemap from "@astrojs/sitemap";

export default defineConfig({
  // The live URL. Needed for the sitemap and for absolute og:image links so
  // shared pages unfurl correctly. Update if the Vercel project name differs.
  site: "https://foraging-texas.vercel.app",

  vite: {
    plugins: [tailwindcss()],
  },

  integrations: [sitemap()],
});