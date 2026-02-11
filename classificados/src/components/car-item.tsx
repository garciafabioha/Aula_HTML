import Link from "next/link";
import Image from "next/image";

type Props = {
    data: {
        id: number;
        title: string;
        img: string;
        priceFrom: number;
        priceTo: number;
    }
}

export const CarItem = ({data}: Props) => {
    return (
        <Link href={`/car/${data.id}`} className="block">
        <Image
            src={`/uploads/${data.img}`}
            alt={data.title}          // acessibilidade ✅
            width={600}              // ajuste conforme seu layout
            height={400}             // ajuste conforme seu layout
            className="w-full rounded object-cover"
            sizes="(max-width: 768px) 100vw, 33vw"  // melhora performance em mobile
        />            
            <p className="text-lg font-bold mt-2">{data.title}</p>
            <p className="text-gray-700 mt-3">De <span className="line-through" >R$ {data.priceFrom.toFixed(2)}</span> por:</p>
            <p className="text-green-700 text-2xl font-bold mt-1">R$ {data.priceTo.toFixed(2)}</p>
        </Link>
    )    
} 