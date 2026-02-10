import { z } from "zod";

export const createCarSchema = z.object({
  title: z.string().min(1, "Título obrigatório"),
  description: z.string().optional(),
  author_name: z.string().min(1, "Nome obrigatório"),
  author_email: z.string().email("Email inválido"),
  negotiable: z.string().optional(),
  price_from: z.string().min(1, "Informe o preço inicial"),
  price_to: z.string().min(1, "Informe o preço atual"),
  img: z
    .instanceof(File)
    .refine((file) => file.size !== 0 && file.name !== undefined)
    .refine((file) => ["image/jpeg", "image/png", "image/webp"].includes(file.type,), "Formato inválido")
    .refine((file) => file.size <= 5242880, "Imagem maior que 5MB"), 
});
