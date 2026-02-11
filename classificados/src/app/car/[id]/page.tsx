// src/app/car/[id]/page.tsx
import { getCarById } from "@/services/car";
import Image from "next/image";

type Props = {
  params: Promise<{ id: string }>;
};

export default async function CarDetail({ params }: Props) {
  const { id } = await params;

  
  const carId = Number(id);
  if (!carId) {
    return <p>ID inválido.</p>;
  }

  const car = await getCarById(carId);

  if (!car) {
    return <p>Carro não encontrado.</p>;
  }

  return (
    <div className="max-w-3xl mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">{car.title}</h1>
      <div className="w-full h-80 relative rounded overflow-hidden">
        <Image
          src={`/uploads/${car.img}`} // ou o campo correto do seu DB
          alt={car.title}
          fill
          className="object-cover rounded"
        />
      </div>
      <p className="mt-4 text-gray-700">{car.description}</p>
      <p className="mt-2 text-lg">
        Autor: {car.authorName} - {car.authorEmail}
      </p>
      <p className="mt-2 text-lg">
        Preço: R$ {car.priceFrom.toFixed(2)} → R$ {car.priceTo.toFixed(2)}
      </p>
      {car.negotiable && <p className="mt-2 text-green-600 font-bold">Negociável</p>}
    </div>
  );
}
