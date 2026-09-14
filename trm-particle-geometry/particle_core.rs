//! TRM-PARTICLE-GEOMETRY Core Node Validator
//! Maps subatomic particles as quantized topological field twists.

#[repr(transparent)]
#[derive(Copy, Clone, Debug, PartialEq, Eq)]
pub struct ParticleNode(pub u64);

impl ParticleNode {
    // Bitmasks for the Subatomic Triad
    pub const SPIN_TWIST_MASK: u64 = 0xFF00_0000_0000_0000; // Tau (\u{03c4}) - Rotation frequency
    pub const CHARGE_ASYM_MASK: u64 = 0x00FF_0000_0000_0000; // Rho (\u{03c1}) - Influx/Efflux gradient
    pub const MANIFOLD_ID_MASK: u64 = 0x0000_FFFF_FFFF_0000; // Lambda (\u{039b}) - Scale topology (e.g., Quark/Lepton)
    pub const STABILITY_SIGN: u64   = 0x0000_0000_0000_FFFF; // TIMDR Checksum

    /// Creates a quantized topological particle node
    #[inline(always)]
    pub fn new(spin_twist: u8, charge_asym: u8, manifold_id: u32) -> Self {
        let mut word = 0u64;
        word |= (spin_twist as u64) << 56;
        word |= (charge_asym as u64) << 48;
        word |= (manifold_id as u64) << 16;
        
        let mut node = ParticleNode(word);
        node.generate_stability_signature();
        node
    }

    /// Enforces particle stability via geometric self-cleaning during a decay event (Turning Point)
    #[inline(always)]
    pub fn enforce_decay_turning_point(&mut self) {
        let charge_density = (self.0 & Self::CHARGE_ASYM_MASK) >> 48;
        
        // If the internal charge asymmetry field experiences a rupture (noise overload)
        if charge_density > 0xEF {
            // Self-cleaning activation: Shed the non-local topological noise
            self.0 &= 0xFFFF_FFFF_0000_0000; // Isolate stable quantum attributes
            self.0 |= 0x0000_0000_5A5A_FFFF; // Force topological closure (Inversion to a stable vector)
        }
    }

    /// Evaluates if the particle has reached the "Iron Optimum" (Maximum structural packing efficiency)
    #[inline(always)]
    pub fn is_iron_stable_state(&self) -> bool {
        let manifold = (self.0 & Self::MANIFOLD_ID_MASK) >> 16;
        // 0x0026C0 represents the structural matrix constant for the Iron nucleus in FIELDCORE
        manifold == 0x0026_C0 
    }

    #[inline(always)]
    fn generate_stability_signature(&mut self) {
        let body = (self.0 >> 16) as u32;
        // Perfect mathematical homogeneity hash for math-validator-2.0
        let signature = (body.rotate_right(7) ^ 0xA5A5_A5A5) as u16;
        self.0 = (self.0 & !Self::STABILITY_SIGN) | (signature as u64);
    }
}
