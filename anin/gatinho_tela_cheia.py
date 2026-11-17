"""Exibe o GIF do gatinho em tela cheia. Pressione Esc para sair."""

from pathlib import Path
import tkinter as tk

GIF_PATH = Path(__file__).with_name("gatin.gif")
FRAME_COUNT = 8
FRAME_DELAY_MS = 70
GIF_SIZE = 500


def main() -> None:
    if not GIF_PATH.is_file():
        raise FileNotFoundError(f"GIF do gatinho não encontrado: {GIF_PATH}")

    janela = tk.Tk()

    def sair_com_esc(evento: tk.Event) -> None:
        if evento.keysym == "Escape":
            janela.destroy()

    janela.title("Gatinho")
    janela.configure(bg="black")
    janela.attributes("-fullscreen", True)
    janela.protocol("WM_DELETE_WINDOW", lambda: None)
    janela.bind_all("<Escape>", sair_com_esc)
    janela.update_idletasks()
    janela.focus_force()

    fator = max(
        1,
        min(
            janela.winfo_screenwidth() // GIF_SIZE,
            janela.winfo_screenheight() // GIF_SIZE,
        ),
    )
    quadros = []
    for indice in range(FRAME_COUNT):
        quadro = tk.PhotoImage(
            master=janela,
            file=str(GIF_PATH),
            format=f"gif -index {indice}",
        )
        quadros.append(quadro.zoom(fator, fator) if fator > 1 else quadro)

    imagem = tk.Label(janela, bg="black", borderwidth=0, image=quadros[0])
    imagem.place(relx=0.5, rely=0.5, anchor="center")

    def animar(indice: int = 0) -> None:
        imagem.configure(image=quadros[indice])
        proximo = (indice + 1) % len(quadros)
        janela.after(FRAME_DELAY_MS, animar, proximo)

    animar()
    janela.mainloop()


if __name__ == "__main__":
    main()
