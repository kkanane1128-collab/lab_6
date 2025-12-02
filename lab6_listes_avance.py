notes = [12, 9, 15, 8, 17, 13, 19, 10]

if not notes:
    print("Aucune note à traiter.")
    exit()
total = 0
for note in notes:
    total += note  

nb_notes = len(notes)
moyenne = total / nb_notes
print(f"Moyenne initiale : {moyenne:.2f}")
notes_bonus = [min(note + 1, 20) for note in notes]
print("Notes après bonus :", notes_bonus)

seuil = 12
notes_valides = [note for note in notes if note >= seuil]
print(f"Notes validées (>= {seuil}) : {notes_valides}")

moyenne_initiale = sum(notes) / nb_notes
moyenne_bonus = sum(notes_bonus) / len(notes_bonus)

lignes = []
lignes.append(" RAPPORT DES NOTES ")
lignes.append(f"Nombre d'étudiants  : {nb_notes}")
lignes.append(f"Moyenne initiale    : {moyenne_initiale:.2f}")
lignes.append(f"Moyenne après bonus : {moyenne_bonus:.2f}")
lignes.append(f"Nombre de validés   : {len(notes_valides)} étudiants (Note >= {seuil})")
lignes.append("-" * 30)
lignes.append("Détails par étudiant :")

for index, note in enumerate(notes, start=1):
    bonus = notes_bonus[index - 1] 
    lignes.append(f"  Étudiant {index:02d} | Note: {note:>5.2f} -> Bonus: {bonus:>5.2f}")

rapport = "\n".join(lignes)

print("\n" + rapport)
with open("rapport_notes.txt", "w", encoding="utf-8") as f:
    f.write(rapport)
    print("\n[Succès] Le rapport a été sauvegardé dans 'rapport_notes.txt'")