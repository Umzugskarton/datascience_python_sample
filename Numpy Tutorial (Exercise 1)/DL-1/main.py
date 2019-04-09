import array_manipulation_warmup.spectrum as spectrum
import array_manipulation_warmup.circle as circle
import array_manipulation_warmup.checkers as checkers
import data_handling_warmup.image_generator as imagegen

if __name__ == "__main__":
    check = checkers.Checker(100, 10)
    check.draw()
    check.show()

    spect = spectrum.Spectrum(500)
    spect.draw()
    spect.show()

    circ = circle.Circle(1000, 150, (200, 500))
    circ.draw()
    circ.show()

    imggen = imagegen.ImageGenerator()
    imggen.show()






