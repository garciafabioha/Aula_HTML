import sharp from "sharp";
import { v4 } from "uuid";

export const fitImage = async (img: File) => {
    const newName = `${v4()}.jpg`;

  const arrayBuffer = await img.arrayBuffer();
  const buffer = Buffer.from(arrayBuffer); // 👈 ESSENCIAL
  
    await sharp(buffer)
    .resize(600, 400, {fit: 'cover'})
    .toFile(`public/uploads/${newName}`);

    return newName;
}