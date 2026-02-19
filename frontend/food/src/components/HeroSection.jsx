const HeroSection = () => {
  return (
  
  <section class="min-h-screen bg-gradient-to-br from-[#FF5C00] via-[#FFA45B] to-[#7ED957] flex flex-col items-center justify-center px-4 py-20 text-center font-sans ">
  <div class="mb-8 flex items-center justify-center">
    <div class="bg-white/30 backdrop-blur-2xl border border-white/20 rounded-full px-6 py-2 text-white text-sm font-medium shadow-xl flex items-center gap-2 mt-10">
      <span class="w-2 h-2 bg-white rounded-full animate-pulse shadow-[0_0_8px_white]"></span>
      Live across 150+ Indian cities
    </div>
  </div>

  <div class="max-w-4xl mx-auto space-y-6">
    <h1 class="text-5xl md:text-7xl font-extrabold text-white leading-tight drop-shadow-md">
      Bridge the Gap <br/> Between Hunger & Hope
    </h1>
    
    <p class="text-white/90 text-lg md:text-xl max-w-2xl mx-auto font-light leading-relaxed">
      Drop a pin. Donate a meal. Claim a cause. Join India's largest crowdsourced movement to ensure no meal goes to waste and no hunger goes unseen.
    </p>

    <div class="flex flex-wrap justify-center gap-4 pt-8">
      <button class="bg-white/10 backdrop-blur-md border border-white/40 text-white px-8 py-4 rounded-xl font-bold hover:bg-white/20 transition-all flex items-center gap-2">
        <svg xmlns="http://www.w3.org" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
        </svg>
        Report Hunger Spot
      </button>

      <button class="bg-white backdrop-blur-md text-[#FF7E33] px-8 py-4 rounded-xl font-bold shadow-2xl hover:scale-105 transition-transform flex items-center gap-2">
        <svg xmlns="http://www.w3.org" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clip-rule="evenodd" />
        </svg>
        Donate Now
      </button>
    </div>
  </div>
  <div class="mt-20 w-full max-w-5xl bg-white/20 backdrop-blur-3xl border border-white/20 rounded-3xl p-8 grid grid-cols-1 md:grid-cols-3 gap-8 shadow-2xl">
    <div class="text-white">
      <h3 class="text-3xl font-bold">12,500+</h3>
      <p class="text-white/70 text-sm">Hunger Spots Identified</p>
    </div>
    <div class="text-white border-x border-white/10 px-4">
      <h3 class="text-3xl font-bold">45,000+</h3>
      <p class="text-white/70 text-sm">Meals Delivered</p>
    </div>
    <div class="text-white">
      <h3 class="text-3xl font-bold">8,200+</h3>
      <p class="text-white/70 text-sm">Active Volunteers</p>
    </div>
  </div>
  </section>
  );
};

export default HeroSection;
