class Himpunan:
    def __init__(self, elements=None):
        # Inisialisasi himpunan tanpa menggunakan `set`
        self.elements = []
        if elements is not None:
            for item in elements:
                if item not in self.elements:
                    self.elements.append(item)

    def __len__(self):
        # Mengembalikan ukuran himpunan
        return len(self.elements)

    def __contains__(self, item):
        # Mengecek apakah item ada dalam himpunan
        return item in self.elements

    def __eq__(self, other):
        # Mengecek apakah dua himpunan memiliki elemen yang sama
        return sorted(self.elements) == sorted(other.elements)

    def __le__(self, other):
        # Mengecek apakah himpunan ini adalah subset dari himpunan lain
        return all(item in other.elements for item in self.elements)

    def __lt__(self, other):
        # Mengecek apakah himpunan ini adalah proper subset dari himpunan lain
        return self <= other and len(self) < len(other)

    def __ge__(self, other):
        # Mengecek apakah himpunan ini adalah superset dari himpunan lain
        return all(item in self.elements for item in other.elements)

    def __floordiv__(self, other):
        # Mengecek apakah dua himpunan ekuivalen
        return sorted(self.elements) == sorted(other.elements)

    def __add__(self, other):
        # Menghitung gabungan (union) dari dua himpunan tanpa duplikasi
        union_elements = self.elements[:]
        for item in other.elements:
            if item not in union_elements:
                union_elements.append(item)
        return Himpunan(union_elements)

    def __sub__(self, other):
        # Menghitung selisih (difference) antara dua himpunan
        return Himpunan([item for item in self.elements if item not in other.elements])

    def __truediv__(self, other):
        # Menghitung irisan (intersection) antara dua himpunan
        return Himpunan([item for item in self.elements if item in other.elements])

    def __mul__(self, other):
        # Menghitung selisih simetris (symmetric difference) antara dua himpunan
        return Himpunan([item for item in self.elements if item not in other.elements] +
                        [item for item in other.elements if item not in self.elements])

    def __pow__(self, other):
        # Menghitung hasil Cartesian product antara dua himpunan
        return [(a, b) for a in self.elements for b in other.elements]

    def add(self, item):
        # Menambahkan item ke dalam himpunan jika belum ada
        if item not in self.elements:
            self.elements.append(item)

    def remove(self, item):
        # Menghapus item dari himpunan jika ada
        if item in self.elements:
            self.elements.remove(item)

    def complement(self, universal_set):
        # Menghitung komplemen dari himpunan ini terhadap himpunan semesta
        return Himpunan([item for item in universal_set.elements if item not in self.elements])

    def __abs__(self):
        # Menghitung himpunan kuasa (power set) tanpa menggunakan `itertools`
        return Himpunan(self.power_set())

    def power_set(self):
        # Menghitung himpunan kuasa (semua subset) secara manual
        subsets = [[]]
        for item in self.elements:
            # Untuk setiap item, tambahkan ke semua subset yang ada
            new_subsets = [subset + [item] for subset in subsets]
            subsets.extend(new_subsets)
        return [Himpunan(subset) for subset in subsets]

    def ListKuasa(self):
        # Menampilkan list dari semua himpunan kuasa yang mungkin
        return self.power_set()

    def __str__(self):
        # Representasi string dari himpunan
        return f"Himpunan({self.elements})"

    def __repr__(self):
        # Representasi resmi untuk debugging dan tampilan himpunan kuasa
        return self.__str__()
