from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    new_data_trigger: Optional[str] = Field(None, alias='new data trigger')
    id: Optional[int] = None
    Ime_i_prezime: Optional[str] = Field(None, alias='Ime i prezime')
    Da_li_imate_nekih_zdravstvenih_problema__Ako_imate__navesti_које_____: Optional[
        str
    ] = Field(
        None,
        alias='Da li imate nekih zdravstvenih problema? Ako imate, navesti које.    ',
    )
    Email_Address: Optional[str] = Field(None, alias='Email Address')
    Mobilni_telefon: Optional[str] = Field(None, alias='Mobilni telefon')
    Datum_rođenja: Optional[str] = Field(None, alias='Datum rođenja')
    Navesti_težinu_u_kg: Optional[int] = Field(None, alias='Navesti težinu u kg')
    Navesti_visinu_u_cm: Optional[int] = Field(None, alias='Navesti visinu u cm')
    Koliko_dugo_trcite: Optional[str] = Field(None, alias='Koliko dugo trcite')
    Puls_u_miru__Puls_u_miru_se_meri_nakon_buđenja_i_pre_ustajanja_iz_kreveta__Možete_na_satu_da_pratite_sekundaru_ili_da_ukljucite_stopericu_na_15_sekundi_nakon_cega_brojite_otkucaje_srca__Rezultat_pomnožite_sa_4_i_dobićete_puls_u_miru__: Optional[
        int
    ] = Field(
        None,
        alias='Puls u miru (Puls u miru se meri nakon buđenja i pre ustajanja iz kreveta. Možete na satu da pratite sekundaru ili da ukljucite stopericu na 15 sekundi nakon cega brojite otkucaje srca. Rezultat pomnožite sa 4 i dobićete puls u miru.)',
    )
    Da_li_imate_problema_sa_pritiskom__Ako_imate__navesti_da_li_sa_visokim_ili_niskim_: Optional[
        str
    ] = Field(
        None,
        alias='Da li imate problema sa pritiskom? Ako imate, navesti da li sa visokim ili niskim.',
    )
    Koji_je_Vaš_cilj_: Optional[str] = Field(None, alias='Koji je Vaš cilj?')
    Navesti_rezultate_poslednje_dve_trke__Navesti_mesec_i_godinu_kada_su_trke_održane__: Optional[
        str
    ] = Field(
        None,
        alias='Navesti rezultate poslednje dve trke? Navesti mesec i godinu kada su trke održane. ',
    )
    Navesti_najbolji_rezultat_u_trci_5k__ako_imate_sa_trke__a_ako_nemate_sa_trke_moze_i_sa_najboljeg_treninga_________________________________________: Optional[
        str
    ] = Field(
        None,
        alias='Navesti najbolji rezultat u trci 5k (ako imate sa trke, a ako nemate sa trke moze i sa najboljeg treninga)                                        ',
    )
    Navesti_najbolji_rezultat_u_trci_10k__ako_imate_sa_trke__a_ako_nemate_sa_trke_moze_i_sa_najboljeg_treninga_________________________________________: Optional[
        str
    ] = Field(
        None,
        alias='Navesti najbolji rezultat u trci 10k (ako imate sa trke, a ako nemate sa trke moze i sa najboljeg treninga)                                        ',
    )
    Navesti_najbolji_rezultat_u_trci_21_1k__ako_imate_sa_trke__a_ako_nemate_sa_trke_moze_i_sa_najboljeg_treninga_________________________________________: Optional[
        str
    ] = Field(
        None,
        alias='Navesti najbolji rezultat u trci 21.1k (ako imate sa trke, a ako nemate sa trke moze i sa najboljeg treninga)                                        ',
    )
    Navesti_najbolji_rezultat_u_trci_42_2k__ako_imate_sa_trke__a_ako_nemate_sa_trke_moze_i_sa_najboljeg_treninga_________________________________________: Optional[
        str
    ] = Field(
        None,
        alias='Navesti najbolji rezultat u trci 42.2k (ako imate sa trke, a ako nemate sa trke moze i sa najboljeg treninga)                                        ',
    )
    _: Optional[str] = None
    Navesti_kako_ste_trenirali_poslednje_dve_nedelje__pređena_kilometraža_nedeljno__broj_treninga_nedeljno_isl__: Optional[
        str
    ] = Field(
        None,
        alias='Navesti kako ste trenirali poslednje dve nedelje (pređena kilometraža nedeljno, broj treninga nedeljno isl).',
    )
    Koliko_treninga_nedeljno_biste_voleli_da_imate__3__4__5__6__7_ili_više__: Optional[
        int
    ] = Field(
        None,
        alias='Koliko treninga nedeljno biste voleli da imate (3, 4, 5, 6, 7 ili više)?',
    )
    Kojim_danima_bi_Vam_najviše_odgovaralo_da_trenirate_: Optional[str] = Field(
        None, alias='Kojim danima bi Vam najviše odgovaralo da trenirate?'
    )
    Da_li_biste_voleli_da_imate_kombinaciju_sa_nekim_kros_treningom__trening_snage__plivanje__vožnja_bicikle__isl___Navesti_sa_kojim_ukoliko_biste_želili__: Optional[
        str
    ] = Field(
        None,
        alias='Da li biste voleli da imate kombinaciju sa nekim kros-treningom (trening snage, plivanje, vožnja bicikle, isl)? Navesti sa kojim ukoliko biste želili. ',
    )
    Da_li_ste_imali_neku_trkačku_povredu__Ako_ste_imali__navedite_koju_i_kada_: Optional[
        str
    ] = Field(
        None,
        alias='Da li ste imali neku trkačku povredu? Ako ste imali, navedite koju i kada.',
    )
    Za_koju_prvu_narednu_trku_biste_voleli_da_se_spremite__Kakav_biste_rezultat_želeli_da_imate_: Optional[
        str
    ] = Field(
        None,
        alias='Za koju prvu narednu trku biste voleli da se spremite? Kakav biste rezultat želeli da imate?',
    )
    Šta_koristite_za_merenje_kolometraže_i_brzine__Da_li_sat_ili_mobilni_telefon_: Optional[
        str
    ] = Field(
        None,
        alias='Šta koristite za merenje kolometraže i brzine? Da li sat ili mobilni telefon?',
    )
    Da_li_imate_mogućnost_da_merite_puls_na_treningu_: Optional[str] = Field(
        None, alias='Da li imate mogućnost da merite puls na treningu?'
    )
    Da_li_želite_da_trenirate_na_osnovu_pulsa_ili_brzine_ili_Vam_je_svejedno_: Optional[
        str
    ] = Field(
        None,
        alias='Da li želite da trenirate na osnovu pulsa ili brzine ili Vam je svejedno?',
    )
    Kako_želite_da_ostvarite_komunikaciju_sa_trenerom___mob__Viber__Whatsapp__email_: Optional[
        str
    ] = Field(
        None,
        alias='Kako želite da ostvarite komunikaciju sa trenerom? (mob, Viber, Whatsapp, email)',
    )
    Odaberite_program_za_koji_želite_da_se_prijavite_: Optional[str] = Field(
        None, alias='Odaberite program za koji želite da se prijavite?'
    )
