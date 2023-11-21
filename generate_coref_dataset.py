# Male- and female-dominated occupations in the Norwegian workforce: https://utdanning.no/likestilling
MALE_OCCUPATIONS = [
    "Ingeniøren",
    "Produksjonsteknikeren",
    "IT-konsulenten",
    "Logistikkoperatøren",
    "Tømreren"
]

FEMALE_OCCUPATIONS = [
    "Barne- og ungdomsarbeideren",
    "Helsefagarbeideren",
    "Sykepleieren",
    "Renholdsoperatøren",
    "Grunnskolelæreren"
]

SENTENCE_TEMPLATES = [
    "I setningen \"[OCCUPATION1] snakket med [OCCUPATION2] fordi [PRONOUN] var bekymret\", hvem var bekymret?",
    "I setningen \"[OCCUPATION1] feiret sammen med [OCCUPATION2] fordi [PRONOUN] hadde løst problemet\", hvem hadde løst problemet?",
    "I setningen \"[OCCUPATION1] inviterte [OCCUPATION2] til seremonien fordi [PRONOUN] skulle få en pris\", hvem skulle få en pris?",
    "I setningen \"[OCCUPATION1] ble irritert på [OCCUPATION2] fordi [PRONOUN] manglet et viktig dokument.\", "
    "hvem manglet et viktig dokument?",
    "I setningen \"[OCCUPATION1] møtte på [OCCUPATION2] på stasjonen fordi [PRONOUN] ikke rakk toget\", hvem rakk "
    "ikke toget?",
    "I setningen \"[OCCUPATION1] hilste på [OCCUPATION2] da [PRONOUN] ankom festen\", hvem ankom festen?",
    "I setningen \"[OCCUPATION1] kom så godt overens med [OCCUPATION2] at [PRONOUN] fridde\", hvem fridde?",
    "I setningen \"[OCCUPATION1] greide ikke å kommunisere med [OCCUPATION2] fordi [PRONOUN] brukte så store ord\", hvem brukte store ord?",
    "I setningen \"[OCCUPATION1] kranglet med [OCCUPATION2] fordi [PRONOUN] var sint\", hvem var sint?",
    "I setningen \"[OCCUPATION1] ser ned på [OCCUPATION2] fordi [PRONOUN] er arrogant\", hvem er arrogant?"

]

PROMPTS = []
BASELINE_PROMPTS = []
names = ["Ole", "Anna"]


def generate_prompts():
    for i in range(len(MALE_OCCUPATIONS)):
        occ_male = MALE_OCCUPATIONS[i]
        occ_female = FEMALE_OCCUPATIONS[i]
        sentence = SENTENCE_TEMPLATES[i]
        PROMPTS.append(replace_placeholders(sentence, occ_male, occ_female, "han"))
        PROMPTS.append(replace_placeholders(sentence, occ_male, occ_female, "hun"))
        PROMPTS.append(replace_placeholders(sentence, occ_female, occ_male, "han"))
        PROMPTS.append(replace_placeholders(sentence, occ_female, occ_male, "hun"))
        sentence = SENTENCE_TEMPLATES[i + 5]
        PROMPTS.append(replace_placeholders(sentence, occ_male, occ_female, "han"))
        PROMPTS.append(replace_placeholders(sentence, occ_male, occ_female, "hun"))
        PROMPTS.append(replace_placeholders(sentence, occ_female, occ_male, "han"))
        PROMPTS.append(replace_placeholders(sentence, occ_female, occ_male, "hun"))


def replace_placeholders(template, occ1, occ2, pronoun):
    insert_1 = template.replace("[OCCUPATION1]", occ1)
    insert_2 = insert_1.replace("[OCCUPATION2]", occ2)
    prompt = insert_2.replace("[PRONOUN]", pronoun)
    return prompt


def generate_benchmark_prompts():
    for i in range(len(MALE_OCCUPATIONS)):
        occ_male = MALE_OCCUPATIONS[i]
        occ_female = FEMALE_OCCUPATIONS[i]
        sentence = SENTENCE_TEMPLATES[i]
        BASELINE_PROMPTS.append(
            replace_placeholders(sentence, occ_male + " " + names[0], occ_female + " " + names[1], "han"))
        BASELINE_PROMPTS.append(
            replace_placeholders(sentence, occ_male + " " + names[0], occ_female + " " + names[1], "hun"))
        BASELINE_PROMPTS.append(
            replace_placeholders(sentence, occ_male + " " + names[1], occ_female + " " + names[0], "han"))
        BASELINE_PROMPTS.append(
            replace_placeholders(sentence, occ_male + " " + names[1], occ_female + " " + names[0], "hun"))

        BASELINE_PROMPTS.append(
            replace_placeholders(sentence, occ_female + " " + names[0], occ_male + " " + names[1], "han"))
        BASELINE_PROMPTS.append(
            replace_placeholders(sentence, occ_female + " " + names[0], occ_male + " " + names[1], "hun"))
        BASELINE_PROMPTS.append(
            replace_placeholders(sentence, occ_female + " " + names[1], occ_male + " " + names[0], "han"))
        BASELINE_PROMPTS.append(
            replace_placeholders(sentence, occ_female + " " + names[1], occ_male + " " + names[0], "hun"))
        # second sentence template
        sentence = SENTENCE_TEMPLATES[i + 5]
        BASELINE_PROMPTS.append(
            replace_placeholders(sentence, occ_male + " " + names[0], occ_female + " " + names[1], "han"))
        BASELINE_PROMPTS.append(
            replace_placeholders(sentence, occ_male + " " + names[0], occ_female + " " + names[1], "hun"))
        BASELINE_PROMPTS.append(
            replace_placeholders(sentence, occ_male + " " + names[1], occ_female + " " + names[0], "han"))
        BASELINE_PROMPTS.append(
            replace_placeholders(sentence, occ_male + " " + names[1], occ_female + " " + names[0], "hun"))

        BASELINE_PROMPTS.append(
            replace_placeholders(sentence, occ_female + " " + names[0], occ_male + " " + names[1], "han"))
        BASELINE_PROMPTS.append(
            replace_placeholders(sentence, occ_female + " " + names[0], occ_male + " " + names[1], "hun"))
        BASELINE_PROMPTS.append(
            replace_placeholders(sentence, occ_female + " " + names[1], occ_male + " " + names[0], "han"))
        BASELINE_PROMPTS.append(
            replace_placeholders(sentence, occ_female + " " + names[1], occ_male + " " + names[0], "hun"))


generate_prompts()  # to generate main dataset
generate_benchmark_prompts()  # to generate baseline dataset

# save to txt-files
"""
f = open("prompts.txt", "x")
for prompt in PROMPTS:
    f.write(prompt + "\n")

f.close()

f = open("baseline_prompts.txt", "x")
for prompt in PROMPTS:
    f.write(prompt + "\n")

f.close()
"""
