import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const plants = defineCollection({
  loader: glob({ pattern: "*.json", base: "./src/content/plants" }),
  schema: ({ image }) =>
    z.object({
      name: z.string(),
      latin: z.string(),
      family: z.string(),
      abundance: z.enum(["abundant", "common", "seasonal", "uncommon"]),
      type: z.enum(["Tree", "Shrub", "Vine", "Ground", "Cactus", "Mushroom", "Aquatic"]),
      uses: z.array(z.enum(["Fruit", "Tea", "Raw", "Cooked", "Nuts", "Flour", "Spice"])),
      regions: z.array(z.enum(["East", "Central", "West"])),
      months: z.array(z.number().int().min(1).max(12)).min(1),
      flowerMonths: z.array(z.number().int().min(1).max(12)).optional(),
      facts: z.object({
        what: z.string(),
        how: z.string(),
        when: z.string(),
        where: z.string(),
        value: z.string(),
      }),
      caution: z.string(),
      sections: z.array(z.object({ title: z.string(), body: z.string() })).min(1),
      similar: z.array(z.string()),
      photos: z
        .array(
          z.object({
            src: image(),
            alt: z.string(),
            credit: z.string(),
            license: z.string(),
            source: z.string(),
          })
        )
        .min(1),
    }),
});

export const collections = { plants };
