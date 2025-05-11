import { defineCollection, z } from 'astro:content';
import { glob, file } from 'astro/loaders';

const images = defineCollection({
    loader: glob({
        pattern: "**/*.json",
        base: "./src/images"}),
        schema: ({ image }) => z.object({
            src: z.string().optional(),
            author: z.string().optional(),
            description: z.string().optional(),
            title: z.string().optional(),
            license: z.string().optional(),
            image: image(),
        })
});

export const collections = { images }