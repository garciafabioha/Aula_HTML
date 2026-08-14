import Link from "next/link"
import { Button } from "./button"

export const Header = () => {
    return (
        <header className="flex justify-between py-10 items-center">
            <div className="text-3xl font-bold">B7Carros</div>
            <div>
                <Link href={"/add"}>
                    <Button label="Cadastrar Carro"/>
                </Link>
            </div>
        </header>
    )    
}