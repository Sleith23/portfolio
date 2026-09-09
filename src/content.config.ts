import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const projects = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/projects" }),
  schema: z.object({
    title: z.string(),
    year: z.string(),
    summary: z.string(),
    role: z.string().optional(),
    stack: z.array(z.string()),
    repo: z.string().url().optional(),
    live: z.string().url().optional(),
    featured: z.boolean().default(false),
    draft: z.boolean().default(false),
    art: z.enum(["grid", "signal", "field", "orbit"]).default("grid"),
  }),
});

const experience = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/experience" }),
  schema: z.object({
    company: z.string(),
    role: z.string(),
    period: z.string(),
    points: z.array(z.string()),
    draft: z.boolean().default(false),
  }),
});

export const collections = { projects, experience };
