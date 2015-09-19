# -*- coding: utf-8 -*-
import scrapy
from amazon.items import AmazonItem


class BestsellersDeptSpider(scrapy.Spider):
    name = "bestsellersdept"
    allowed_domains = ["amazon.com"]
    start_urls = [
        # 'https://www.amazon.com/Best-Sellers-Appliances/zgbs/appliances/',
        # 'https://www.amazon.com/Best-Sellers-Arts-Crafts-Sewing/zgbs/arts-crafts/',
        # 'https://www.amazon.com/Best-Sellers-Automotive/zgbs/automotive/',
        # 'https://www.amazon.com/Best-Sellers-Baby/zgbs/baby-products/',
        # 'https://www.amazon.com/Best-Sellers-Cell-Phones-Accessories/zgbs/wireless/',
        # 'https://www.amazon.com/Best-Sellers-Computers-Accessories/zgbs/pc/',
        # 'https://www.amazon.com/Best-Sellers-Health-Personal-Care/zgbs/hpc/',
        # 'https://www.amazon.com/Best-Sellers-Home-Kitchen/zgbs/home-garden/',
        # 'https://www.amazon.com/Best-Sellers-Home-Improvement/zgbs/hi/',
        # 'https://www.amazon.com/Best-Sellers-Industrial-Scientific/zgbs/industrial/',
        # 'https://www.amazon.com/Best-Sellers-Kitchen-Dining/zgbs/kitchen/',
        # 'https://www.amazon.com/Best-Sellers-Musical-Instruments/zgbs/musical-instruments/',
        # 'https://www.amazon.com/Best-Sellers-Office-Products/zgbs/office-products/',
        # 'https://www.amazon.com/Best-Sellers-Patio-Lawn-Garden/zgbs/lawn-garden/',
        # 'https://www.amazon.com/Best-Sellers-Pet-Supplies/zgbs/pet-supplies/',
        # 'https://www.amazon.com/Best-Sellers-Sports-Outdoors/zgbs/sporting-goods
        'http://www.amazon.com/Best-Sellers-Sports-Outdoors/zgbs/sporting-goods/ref=zg_bs_nav_0',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Outdoor-Recreation/zgbs/sporting-goods/706814011/ref=zg_bs_nav_sg_1_sg',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Camping-Hiking-Equipment/zgbs/sporting-goods/3400371/ref=zg_bs_nav_sg_2_706814011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Hiking-Backpacks-Bags/zgbs/sporting-goods/3400391/ref=zg_bs_nav_sg_3_3400371',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Camping-Tents-Shelters/zgbs/sporting-goods/10208056011/ref=zg_bs_nav_sg_3_3400371',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Camping-Shelters/zgbs/sporting-goods/3401821/ref=zg_bs_nav_sg_4_10208056011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Camping-Screen-Houses-Rooms/zgbs/sporting-goods/10208057011/ref=zg_bs_nav_sg_6_10208168011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Camping-Sun-Shelters/zgbs/sporting-goods/3258963011/ref=zg_bs_nav_sg_6_10208057011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Sleeping-Bags-Camp-Bedding/zgbs/sporting-goods/3401611/ref=zg_bs_nav_sg_3_3400371',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Camp-Kitchen-Equipment/zgbs/sporting-goods/2204505011/ref=zg_bs_nav_sg_3_3400371',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Backpacking-Camping-Stoves-Grills/zgbs/sporting-goods/3400941/ref=zg_bs_nav_sg_4_2204505011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Camping-Stove-Accessories/zgbs/sporting-goods/3401021/ref=zg_bs_nav_sg_4_2204505011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Camping-Cooking-Utensils/zgbs/sporting-goods/3400601/ref=zg_bs_nav_sg_5_3400721',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Camping-Cooler-Accessories/zgbs/sporting-goods/14329861/ref=zg_bs_nav_sg_5_14335431',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Camping-Dishes-Utensils/zgbs/sporting-goods/3400701/ref=zg_bs_nav_sg_5_14329861',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Camping-Hiking-Hydration-Filtration-Products/zgbs/sporting-goods/2204506011/ref=zg_bs_nav_sg_3_3400371',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Camping-Hiking-Hydration-Flasks/zgbs/sporting-goods/3402071/ref=zg_bs_nav_sg_4_2204506011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Camping-Knives-Tools/zgbs/sporting-goods/3400851/ref=zg_bs_nav_sg_3_3400371',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Camping-Safety-Survival-Equipment/zgbs/sporting-goods/3401081/ref=zg_bs_nav_sg_3_3400371',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Camping-Signal-Whistles/zgbs/sporting-goods/2204653011/ref=zg_bs_nav_sg_4_3401081',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Climbing-Equipment/zgbs/sporting-goods/3402401/ref=zg_bs_nav_sg_2_706814011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Outdoor-Recreation/zgbs/sporting-goods/706814011/ref=zg_bs_unv_sg_2_3402401_1',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Climbing-Rope-Cord-Webbing/zgbs/sporting-goods/3402821/ref=zg_bs_nav_sg_3_3402401',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Climbing-Slings-Runners/zgbs/sporting-goods/2368083011/ref=zg_bs_nav_sg_4_3402821',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Climbing-Rope/zgbs/sporting-goods/3402851/ref=zg_bs_nav_sg_5_3402871',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Climbing-Harnesses/zgbs/sporting-goods/3402661/ref=zg_bs_nav_sg_3_3402401',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Climbing-Hardware/zgbs/sporting-goods/3402481/ref=zg_bs_nav_sg_3_3402401',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Climbing-Ascenders/zgbs/sporting-goods/3402501/ref=zg_bs_nav_sg_4_3402481',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Climbing-Belay-Rappel-Equipment/zgbs/sporting-goods/3402511/ref=zg_bs_nav_sg_5_3402501',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Climbing-Pulleys/zgbs/sporting-goods/3402641/ref=zg_bs_nav_sg_5_3402511',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Climbing-Carabiners-Quickdraws/zgbs/sporting-goods/3402541/ref=zg_bs_nav_sg_3_3402401',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Locking-Climbing-Carabiners/zgbs/sporting-goods/3402551/ref=zg_bs_nav_sg_4_3402541',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Nonlocking-Climbing-Carabiners/zgbs/sporting-goods/3402561/ref=zg_bs_nav_sg_5_3402551',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Quickdraw-Climbing-Carabiners/zgbs/sporting-goods/3402571/ref=zg_bs_nav_sg_5_3402561',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Climbing-Helmets/zgbs/sporting-goods/3402801/ref=zg_bs_nav_sg_3_3402401',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Fitness/zgbs/sporting-goods/10971181011/ref=zg_bs_nav_sg_1_sg',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Exercise-Fitness-Equipment/zgbs/sporting-goods/3407731/ref=zg_bs_nav_sg_2_10971181011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Strength-Training-Equipment/zgbs/sporting-goods/3408271/ref=zg_bs_nav_sg_3_3407731',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Strength-Training-Ankle-Weights/zgbs/sporting-goods/3408291/ref=zg_bs_nav_sg_4_3408271',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Strength-Training-Arm-Machines/zgbs/sporting-goods/3408311/ref=zg_bs_nav_sg_5_3408291',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Strength-Training-Back-Machines/zgbs/sporting-goods/3408321/ref=zg_bs_nav_sg_5_3408311',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Strength-Training-Bars/zgbs/sporting-goods/3408331/ref=zg_bs_nav_sg_5_3408321',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Core-Strength-Abdominal-Trainers/zgbs/sporting-goods/3408281/ref=zg_bs_nav_sg_4_3408271',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Strength-Training-Dip-Stands/zgbs/sporting-goods/3408391/ref=zg_bs_nav_sg_5_3408281',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Exercise-Fitness-Dumbbells/zgbs/sporting-goods/3408401/ref=zg_bs_nav_sg_5_3408391',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Strength-Training-Hand-Strengtheners/zgbs/sporting-goods/14333021/ref=zg_bs_nav_sg_5_3408401',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Exercise-Fitness-Home-Gyms/zgbs/sporting-goods/3408411/ref=zg_bs_nav_sg_5_14333021',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Strength-Training-Inversion-Equipment/zgbs/sporting-goods/3408421/ref=zg_bs_nav_sg_5_3408411',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Strength-Training-Kettlebells/zgbs/sporting-goods/16385851/ref=zg_bs_nav_sg_5_3408421',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Strength-Training-Leg-Machines/zgbs/sporting-goods/3408431/ref=zg_bs_nav_sg_5_16385851',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Strength-Training-Pull-Up-Bars/zgbs/sporting-goods/3408471/ref=zg_bs_nav_sg_5_3408441',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Strength-Training-Pushup-Stands/zgbs/sporting-goods/3408481/ref=zg_bs_nav_sg_5_3408471',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Strength-Training-Smith-Machines/zgbs/sporting-goods/3408491/ref=zg_bs_nav_sg_5_3408481',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Weight-Lifting-Belts/zgbs/sporting-goods/2403095011/ref=zg_bs_nav_sg_5_3408491',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Strength-Training-Weight-Racks/zgbs/sporting-goods/3408511/ref=zg_bs_nav_sg_5_2403095011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Strength-Training-Weight-Vests/zgbs/sporting-goods/3408561/ref=zg_bs_nav_sg_4_3408271',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Strength-Training-Weights/zgbs/sporting-goods/16385861/ref=zg_bs_nav_sg_5_3408561',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Strength-Training-Wrist-Weights/zgbs/sporting-goods/3408571/ref=zg_bs_nav_sg_5_16385861',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Treadmill-Belts/zgbs/sporting-goods/1260446011/ref=zg_bs_nav_sg_4_1260445011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Balance-Trainers/zgbs/sporting-goods/3407851/ref=zg_bs_nav_sg_3_3407731',


'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Balance-Boards/zgbs/sporting-goods/3407861/ref=zg_bs_nav_sg_4_3407851',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Foam-Rollers/zgbs/sporting-goods/3407871/ref=zg_bs_nav_sg_5_3407861',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Swiss-Balls/zgbs/sporting-goods/3407881/ref=zg_bs_nav_sg_5_3407871',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Golf-Club-Parts/zgbs/sporting-goods/3410911/ref=zg_bs_nav_sg_3_3410851',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Golf-Cart-Accessories/zgbs/sporting-goods/3410871/ref=zg_bs_nav_sg_3_3410851',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Golf-Club-Bag-Accessories/zgbs/sporting-goods/3411271/ref=zg_bs_nav_sg_4_3410871',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Course-Golf-Accessories/zgbs/sporting-goods/3411021/ref=zg_bs_nav_sg_4_3411271',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Golf-Ball-Markers/zgbs/sporting-goods/3411031/ref=zg_bs_nav_sg_4_3411021',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Golf-Tees/zgbs/sporting-goods/3411071/ref=zg_bs_nav_sg_5_3411031',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Hunting-Fishing/zgbs/sporting-goods/706813011/ref=zg_bs_nav_sg_2_10971181011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Leisure-Games-Equipment/zgbs/sporting-goods/706808011/ref=zg_bs_nav_sg_2_10971181011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Arcade-Table-Games/zgbs/sporting-goods/7427858011/ref=zg_bs_nav_sg_3_706808011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Air-Hockey-Tables-Equipment/zgbs/sporting-goods/3419221/ref=zg_bs_nav_sg_4_7427858011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Combination-Game-Tables/zgbs/sporting-goods/13281691/ref=zg_bs_nav_sg_5_3419221',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Foosball-Tables-Equipment/zgbs/sporting-goods/2341347011/ref=zg_bs_nav_sg_5_3419241',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Pong-Games/zgbs/sporting-goods/7427906011/ref=zg_bs_nav_sg_5_3419271',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Shuffleboard-Equipment/zgbs/sporting-goods/2341346011/ref=zg_bs_nav_sg_5_7427906011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Tabletop-Table-Tennis-Games/zgbs/sporting-goods/7427910011/ref=zg_bs_nav_sg_5_7427908011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Running-Equipment/zgbs/sporting-goods/3416071/ref=zg_bs_nav_sg_2_10971181011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Running-Hydration-Packs/zgbs/sporting-goods/672093011/ref=zg_bs_nav_sg_4_3416071',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Reflective-Gear/zgbs/sporting-goods/3395071/ref=zg_bs_nav_sg_5_672093011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Running-Waist-Packs/zgbs/sporting-goods/672097011/ref=zg_bs_nav_sg_5_672093011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-GPS-Units/zgbs/sporting-goods/219536011/ref=zg_bs_unv_sg_5_617647011_1',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Running-Footwear/zgbs/sporting-goods/2226243011/ref=zg_bs_nav_sg_5_672093011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Swimming-Equipment/zgbs/sporting-goods/3418761/ref=zg_bs_nav_sg_2_10971181011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Swimming-Aquatic-Gloves/zgbs/sporting-goods/3418781/ref=zg_bs_nav_sg_3_3418761',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Swimming-Earplugs/zgbs/sporting-goods/3418811/ref=zg_bs_nav_sg_3_3418761',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Swimming-Goggles/zgbs/sporting-goods/3418871/ref=zg_bs_nav_sg_3_3418761',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Swimming-Nose-Clips/zgbs/sporting-goods/3418821/ref=zg_bs_nav_sg_3_3418761',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Swimming-Caps/zgbs/sporting-goods/3418961/ref=zg_bs_nav_sg_3_3418761',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Swimming-Fins/zgbs/sporting-goods/3419061/ref=zg_bs_nav_sg_3_3418761',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Swimming-Training-Equipment/zgbs/sporting-goods/3419101/ref=zg_bs_nav_sg_3_3418761',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Team/zgbs/sporting-goods/706809011/ref=zg_bs_nav_sg_2_10971181011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Tennis-Racquet-Sport-Equipment/zgbs/sporting-goods/706816011/ref=zg_bs_nav_sg_2_10971181011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Badminton-Equipment/zgbs/sporting-goods/3528171/ref=zg_bs_nav_sg_4_706816011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Handball-Equipment/zgbs/sporting-goods/14335791/ref=zg_bs_nav_sg_4_706816011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Racquetball-Equipment/zgbs/sporting-goods/3528161/ref=zg_bs_nav_sg_4_706816011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Squash-Equipment/zgbs/sporting-goods/13280811/ref=zg_bs_nav_sg_4_706816011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Tennis-Equipment/zgbs/sporting-goods/3419511/ref=zg_bs_nav_sg_4_706816011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Yoga-Equipment/zgbs/sporting-goods/3422251/ref=zg_bs_nav_sg_2_10971181011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Other-Types/zgbs/sporting-goods/706810011/ref=zg_bs_nav_sg_2_10971181011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Accessories/zgbs/sporting-goods/3394801/ref=zg_bs_nav_sg_2_10971181011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Athletic-Tapes-Wraps/zgbs/sporting-goods/3775561/ref=zg_bs_nav_sg_4_3422351',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Mouthguards/zgbs/sporting-goods/3410701/ref=zg_bs_nav_sg_5_3775561',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Athletic-Padding-Supplies/zgbs/sporting-goods/3422511/ref=zg_bs_nav_sg_5_3410701',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Yoga-Towels/zgbs/sporting-goods/7261122011/ref=zg_bs_nav_sg_4_3422251',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Yoga-Blocks/zgbs/sporting-goods/3422271/ref=zg_bs_nav_sg_4_3422251',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Yoga-Clothing/zgbs/sporting-goods/2371064011/ref=zg_bs_nav_sg_4_3422251',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Yoga-Foam-Wedges/zgbs/sporting-goods/3422281/ref=zg_bs_nav_sg_4_3422251',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Yoga-Mat-Bags/zgbs/sporting-goods/1240801011/ref=zg_bs_nav_sg_4_3422251',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Yoga-Mats/zgbs/sporting-goods/3422301/ref=zg_bs_nav_sg_4_3422251',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Yoga-Silk-Eye-Bags/zgbs/sporting-goods/3422321/ref=zg_bs_nav_sg_4_3422251',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Yoga-Starter-Sets/zgbs/sporting-goods/3422331/ref=zg_bs_nav_sg_4_3422251',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Yoga-Straps/zgbs/sporting-goods/3422341/ref=zg_bs_nav_sg_4_3422251',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Martial-Arts-Equipment/zgbs/sporting-goods/3415011/ref=zg_bs_nav_sg_3_706810011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Martial-Arts-Training-Equipment/zgbs/sporting-goods/3415021/ref=zg_bs_nav_sg_4_3415011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Martial-Arts-Hand-Targets-Focus-Mitts/zgbs/sporting-goods/3415071/ref=zg_bs_nav_sg_5_3415021',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Martial-Arts-Kicking-Shields/zgbs/sporting-goods/3415081/ref=zg_bs_nav_sg_6_3415071',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Martial-Arts-Kicking-Targets/zgbs/sporting-goods/3415091/ref=zg_bs_nav_sg_6_3415081',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Martial-Arts-Training-Gloves/zgbs/sporting-goods/13280551/ref=zg_bs_nav_sg_6_3415091',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Martial-Arts-Training-Sticks/zgbs/sporting-goods/3415161/ref=zg_bs_nav_sg_6_13280551',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Martial-Arts-Targets/zgbs/sporting-goods/3415141/ref=zg_bs_nav_sg_6_3415161',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Martial-Arts-Bag-Gloves/zgbs/sporting-goods/3415031/ref=zg_bs_nav_sg_6_3415141',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Martial-Arts-Protective-Gear/zgbs/sporting-goods/3415211/ref=zg_bs_nav_sg_4_3415011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Martial-Arts-Weapons/zgbs/sporting-goods/3415301/ref=zg_bs_nav_sg_4_3415011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Martial-Arts-Weapon-Stands/zgbs/sporting-goods/3415181/ref=zg_bs_nav_sg_4_3415011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Martial-Arts-Weapon-Cases/zgbs/sporting-goods/3415171/ref=zg_bs_nav_sg_5_3415181',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Martial-Arts-Belt-Pins/zgbs/sporting-goods/3415051/ref=zg_bs_nav_sg_5_3415171',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Martial-Arts-Belt-Displays/zgbs/sporting-goods/3415041/ref=zg_bs_nav_sg_5_3415051',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Martial-Arts-Equipment-Bags/zgbs/sporting-goods/3415061/ref=zg_bs_nav_sg_5_3415041',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Martial-Arts-Clothing/zgbs/sporting-goods/2368086011/ref=zg_bs_nav_sg_5_3415061',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Boxing-Equipment/zgbs/sporting-goods/3400051/ref=zg_bs_nav_sg_3_706810011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Boxing-Gloves/zgbs/sporting-goods/3400071/ref=zg_bs_nav_sg_4_3400051',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Punch-Mitts/zgbs/sporting-goods/3400121/ref=zg_bs_nav_sg_4_3400051',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Punching-Bag-Accessories/zgbs/sporting-goods/3400301/ref=zg_bs_nav_sg_5_3400121',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Ballet-Dance-Equipment/zgbs/sporting-goods/13285461/ref=zg_bs_nav_sg_3_706810011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Ballet-Equipment/zgbs/sporting-goods/13285471/ref=zg_bs_nav_sg_4_13285461',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Tap-Dancing-Equipment/zgbs/sporting-goods/13285551/ref=zg_bs_nav_sg_5_13285471',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Ballet-Dance-Footwear/zgbs/sporting-goods/13285581/ref=zg_bs_nav_sg_5_13285521',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Equestrian-Equipment/zgbs/sporting-goods/3407321/ref=zg_bs_nav_sg_3_706810011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Fencing-Equipment/zgbs/sporting-goods/13286711/ref=zg_bs_nav_sg_3_706810011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Fencing-Lam%C3%A9s/zgbs/sporting-goods/13286871/ref=zg_bs_nav_sg_5_13286711',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Fencing-Protective-Gear/zgbs/sporting-goods/13286901/ref=zg_bs_nav_sg_6_13286871',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Fencing-Training-Equipment/zgbs/sporting-goods/5731890011/ref=zg_bs_nav_sg_5_13286711',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Fencing-Weapons-Parts/zgbs/sporting-goods/13286991/ref=zg_bs_nav_sg_5_13286711',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Gymnastics-Equipment/zgbs/sporting-goods/3412011/ref=zg_bs_nav_sg_3_706810011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Gymnastics-Gym-Competition-Equipment/zgbs/sporting-goods/3412151/ref=zg_bs_nav_sg_4_3412011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Gymnastics-Asymmetric-Bars/zgbs/sporting-goods/3412161/ref=zg_bs_nav_sg_5_3412151',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Gymnastics-Mats-Flooring/zgbs/sporting-goods/5714220011/ref=zg_bs_nav_sg_4_3412011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Gymnastics-Rings/zgbs/sporting-goods/3412221/ref=zg_bs_nav_sg_5_3412151',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Gymnastics-Accessories/zgbs/sporting-goods/5714219011/ref=zg_bs_nav_sg_5_13280201',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Wristbands/zgbs/sporting-goods/3419981/ref=zg_bs_nav_sg_3_3394801',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Vehicle-Racks-Carriers/zgbs/sporting-goods/491437011/ref=zg_bs_nav_sg_3_3394801',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Coach-Referee-Umpire-Gear/zgbs/sporting-goods/3394821/ref=zg_bs_nav_sg_3_3394801',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Field-Court-Gym-Rink-Equipment/zgbs/sporting-goods/2344448011/ref=zg_bs_nav_sg_3_3394801',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Outdoor-Gear-Repair-Equipment/zgbs/sporting-goods/10208184011/ref=zg_bs_nav_sg_3_3394801',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Inflation-Devices-Accessories/zgbs/sporting-goods/2341089011/ref=zg_bs_nav_sg_4_10208184011',

'http://www.amazon.com/Best-Sellers-Sports-Outdoors-Headbands/zgbs/sporting-goods/719962011/ref=zg_bs_nav_sg_3_3394801'       
    ]

    # def parse(self, response):
    #     for href in response.xpath('//ul[@id="zg_browseRoot"]/ul/li/a/@href'):
    #         url = str(href.extract()).strip()
    #         # yield scrapy.Request(url, callback=self.parse_pagination)
    #         yield scrapy.Request(url, callback=self.parse_category) 

    #renamed parse to parse_category

    # def parse(self, response):
    #     for href in response.xpath(
    #         '//ul[@id="zg_browseRoot"]/ul/ul/li/a/@href'
    #     ):
    #         url = str(href.extract()).strip()
    #         print url
    #         yield scrapy.Request(url, callback=self.parse_pagination)

    #rename parse to parse_pagination

    def parse(self, response):
        for href in response.css('ol.zg_pagination a::attr(href)'):
            url = str(href.extract()).strip()
            yield scrapy.Request(url, callback=self.parse_item_link)

    def parse_item_link(self, response):
        for href in response.css('div.zg_title a::attr(href)'):
            url = str(href.extract()).strip()
            yield scrapy.Request(url, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        product = AmazonItem()
        product['name'] = response.css('h1 span.a-size-large::text').extract()
        product['url'] = response.url

        if response.xpath('//tr[@id="SalesRank"]/td[@class="value"]/text()').re_first('\d+,*\d*d*d*') == None:
            product['departmentRank'] = response.xpath('//li[@id="SalesRank"]/text()').re_first('\d+,*\d*d*d*')
        else: 
            product['departmentRank'] = response.xpath('//tr[@id="SalesRank"]/td[@class="value"]/text()').re_first('\d+,*\d*d*d*')

        try:
            product['department'] = str(response.xpath(
                '''//div[@id="wayfinding-breadcrumbs_feature_div"]
                /ul/li/span/a/text()''').extract()[0]).strip()
        except IndexError:
            pass

        try:
            product['subDepartment'] = str(response.xpath(
                '''//div[@id="wayfinding-breadcrumbs_feature_div"]
                /ul/li/span/a/text()''').extract()[1]).strip()
        except IndexError:
            pass
        try:
            product['price'] = response.css(
                'td span.a-color-price::text').re('^[$]\d+\.\d+')[0]
        except IndexError:
            pass
        try:
            product['reviews'] = response.css(
                '''div.feature div.a-spacing-none span.a-declarative
                 span.a-size-base::text''').re('\d+,*\d*d*d*')[0]
        except IndexError:
            pass

        
        if response.xpath('//tr/td[@class="bucket"]/div[@class="content"]/ul/li[contains(.,"Shipping Weight")]').re('\d.*pounds|ounces') == []:
            try:
                product['weight'] = response.css(
                    'tr.size-weight td.value::text').extract()[0]
            except IndexError:
                pass
        else:
            product['weight'] = response.xpath('//tr/td[@class="bucket"]/div[@class="content"]/ul/li[contains(.,"Shipping Weight")]').re('\d.*pounds|\d.*ounces')

        if response.xpath('//tr/td[@class="bucket"]/div[@class="content"]/ul/li[contains(.,"Dimensions")]').re('\d.*inches') == []:
            try:
                product['dimensions'] = response.css(
                    'tr.size-weight td.value::text').extract()[1]
            except IndexError:
                pass
        else:
            product['dimensions'] = response.xpath('//tr/td[@class="bucket"]/div[@class="content"]/ul/li[contains(.,"Dimensions")]').re('\d.*inches')

        yield product
